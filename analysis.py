import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from database import pasirinkti_ligos_duomenis

table_name = 'ligu_duomenys'
columns = ['_id', 'centras', 'registravimo_vieta', 'miestas', 'galutine_diagnoze', 'ligonis_hospitalizuotas', 'socialiai_apdraustas', 'infekcijos_tipas', 'is_salies', 'ligos_klinikine_eiga', 'atvyk', 'kreip_diag', 'pranesimo_menuo', 'mirtis', 'sukelejo_rusis']
conditions = ""
conn_params = {
    'dbname': 'ligos',
    'user': 'postgres',
    'password': 'Y1IOpBVejMxDkNE',
    'port': 5432,
    'host': 'localhost'
}

# print(pasirinkti_ligos_duomenis(conn_params, table_name, columns, conditions))

ligu_duombaze = pasirinkti_ligos_duomenis(conn_params, table_name, columns, conditions)

# print(ligu_duombaze.groupby('sukelejo_rusis').size())
# print(ligu_duombaze.groupby('mirtis').size())
# print(ligu_duombaze.groupby('socialiai_apdraustas').size())
# print(ligu_duombaze.groupby('pranesimo_menuo').size())

# ligu_duombaze[ligu_duombaze["galutine_diagnoze"] =="Vėjaraupiai"]
# print(ligu_duombaze.groupby("galutine_diagnoze").size().reset_index(name='count').nlargest(10, "count"))

def diagnoziu_kiekis_pagal_menesi(gal_diag):
    return ligu_duombaze[ligu_duombaze["galutine_diagnoze"] == gal_diag].groupby("pranesimo_menuo").size().reset_index(name='count')
# print(diagnoziu_kiekis_pagal_menesi("Lėtinis virusinis hepatitas C"))


df = diagnoziu_kiekis_pagal_menesi('Plaučių tuberkuliozė, patvirtinta skreplių mikroskopijos, su bakterijų kultūra ar be jos').set_index('pranesimo_menuo')


temp_dict = df.to_dict()

for i in range(2010,2024):
    for j in range (1,13):
        if datetime.date(i,j,1) not in temp_dict['count']:
            temp_dict['count'][datetime.date(i,j,1)] = 0
print('Galinis laikinas sarasas\n',temp_dict)
fixed_df = pd.DataFrame.from_dict(temp_dict).reset_index(names=['pranesimo_menuo', 'count'])
# fixed_df = fixed_df.set_index('men_pav')
print('Pataisytas dataframe\n',fixed_df)


fixed_df["pranesimo_menuo"]=pd.to_datetime(fixed_df["pranesimo_menuo"])

temp_df = pd.DataFrame()
for i in range(2010,2024):
    temp_df[f'{i}'] = fixed_df[fixed_df['pranesimo_menuo'].dt.year == i]['count'].values
men_pav = ['Sausis', 'Vasaris', 'Kovas', 'Balandis','Gegužė', 'Birželis', 'Liepa', 'Rugpjūtis', 'Rugsėjis', 'Spalis', 'Lapkritis', 'Gruodis']
temp_df['mėnesis'] = men_pav
temp_df = temp_df.set_index('mėnesis')
print(temp_df)

temp_df.plot.line(ylabel='Užsikrėtimų skaičius')
plt.show()





# diagnoziu_kiekis_pagal_menesi('Vėjaraupiai').plot.line(x='pranesimo_menuo', y='count', c='DarkBlue')
# plt.show()
#
# df = diagnoziu_kiekis_pagal_menesi('Rotavirusų sukeltas enteritas')
# df["pranesimo_menuo"]=pd.to_datetime(df["pranesimo_menuo"])
# df[df['pranesimo_menuo'].dt.year==2020].plot.line(x='pranesimo_menuo', y='count', c='DarkBlue')
# plt.show()



# df = pd.DataFrame(ligu_duombaze.groupby("galutine_diagnoze").size().reset_index(name='count').nlargest(10, "count"))
# print(df)

# data = ['47997', '23790', '16166', '15740', '12531']
# labels = ['Rotavirusų sukeltas enteritas', 'Vėjaraupiai be komplikacijų', 'Kampilobakterijų sukeltas enteritas', 'Salmonelių sukeltas enteritas', 'Norovirusų (Norvalko (Norwalk) veiksnio)\n sukeltas ūminis gastroenteritas']
# plt.figure(figsize = (15,10))
# palette_color = sns.color_palette("deep")
# plt.pie(data, labels=labels, colors=palette_color, autopct='%.0f%%', textprops={'fontsize': 12})
# plt.show()

