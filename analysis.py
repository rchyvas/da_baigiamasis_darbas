import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import numpy as np
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
# print(ligu_duombaze.groupby('ligonis_hospitalizuotas').size())

ligu_duombaze[ligu_duombaze["galutine_diagnoze"] =="Vėjaraupiai"]
print(ligu_duombaze.groupby("galutine_diagnoze").size().reset_index(name='count').nlargest(10, "count"))


pie_df = ligu_duombaze.groupby('galutine_diagnoze').size().reset_index(name='count').nlargest(5, "count").set_index('galutine_diagnoze')
print(pie_df)
palette_color = sns.color_palette("deep")
pie_df.plot.pie(y = 'count', colors=palette_color, autopct='%.0f%%',legend=False, figsize = (30,10), textprops={'fontsize': 22})
plt.ylabel('')
plt.show()

def diagnoziu_kiekis_pagal_menesi(gal_diag):
    return ligu_duombaze[ligu_duombaze["galutine_diagnoze"] == gal_diag].groupby("pranesimo_menuo").size().reset_index(name='count')
# # print(diagnoziu_kiekis_pagal_menesi("Lėtinis virusinis hepatitas C"))
#
menesiu_stulpelis = ligu_duombaze.groupby("pranesimo_menuo").size().reset_index(name='count').drop('count',axis=1)

df_tot=pd.DataFrame(menesiu_stulpelis)
pop_ligos = ['Rotavirusų sukeltas enteritas', 'Vėjaraupiai be komplikacijų', 'Kampilobakterijų sukeltas enteritas', 'Salmonelių sukeltas enteritas', 'Norovirusų (Norvalko (Norwalk) veiksnio) sukeltas ūminis gastroenteritas ']
for liga in pop_ligos:
    df = diagnoziu_kiekis_pagal_menesi(liga).set_index('pranesimo_menuo')
    temp_dict = df.to_dict()
    for i in range(2010,2024):
        for j in range (1,13):
            if datetime.date(i,j,1) not in temp_dict['count']:
                temp_dict['count'][datetime.date(i,j,1)] = 0
    fixed_df = pd.DataFrame.from_dict(temp_dict).reset_index(names=['pranesimo_menuo', 'count'])
    df_tot[liga] = fixed_df['count']

df_tot.set_index('pranesimo_menuo').plot.line(ylabel='Užsikrėtimų skaičius')
plt.xlabel('Pranešimo mėnuo')
plt.legend(fontsize="8", loc = "upper right")
plt.show()

df = diagnoziu_kiekis_pagal_menesi('Rotavirusų sukeltas enteritas').set_index('pranesimo_menuo')
#
temp_dict = df.to_dict()

for i in range(2010,2024):
    for j in range (1,13):
        if datetime.date(i,j,1) not in temp_dict['count']:
            temp_dict['count'][datetime.date(i,j,1)] = 0
print('Galinis laikinas sarasas\n',temp_dict)
fixed_df = pd.DataFrame.from_dict(temp_dict).reset_index(names=['pranesimo_menuo', 'count'])
# fixed_df = fixed_df.set_index('men_pav')
print('Pataisytas dataframe\n',fixed_df)
#
#
fixed_df["pranesimo_menuo"]=pd.to_datetime(fixed_df["pranesimo_menuo"])
#
temp_df = pd.DataFrame()
for i in range(2010,2024):
    temp_df[f'{i}'] = fixed_df[fixed_df['pranesimo_menuo'].dt.year == i]['count'].values
men_pav = ['Sausis', 'Vasaris', 'Kovas', 'Balandis','Gegužė', 'Birželis', 'Liepa', 'Rugpjūtis', 'Rugsėjis', 'Spalis', 'Lapkritis', 'Gruodis']
temp_df['mėnesis'] = men_pav
temp_df = temp_df.set_index('mėnesis')
print(temp_df)

temp_df.plot.line(ylabel='Užsikrėtimų skaičius', figsize = (8,8))
font1 = {'size': 14}
plt.title("Rotavirusų sukeltas enteritas", fontdict = font1)
plt.show()

def hospitalizavimo_kiekis_pagal_liga(gal_diag):
    return ligu_duombaze[ligu_duombaze["galutine_diagnoze"] == gal_diag].groupby("ligonis_hospitalizuotas").size().reset_index(name='count')
# # print(hospitalizavimo_kiekis_pagal_liga("Norovirusų (Norvalko (Norwalk) veiksnio) sukeltas ūminis gastroenteritas "))

plt.rcParams["figure.figsize"] = (10, 10)
x = ['Rotavirusų\n sukeltas\n enteritas', 'Vėjaraupiai\n be komplikacijų', 'Kampilobakterijų\n sukeltas\n enteritas', 'Salmonelių\n sukeltas\n enteritas', 'Norovirusų (Norvalko\n (Norwalk) veiksnio) sukeltas\n ūminis gastroenteritas']
y1 = np.array([45638, 138, 11689, 12184, 11570])
y2 = np.array([2359, 23652, 4477, 3556, 961])

plt.bar(x, y1, color = '#800000')
plt.bar(x, y2, bottom=y1, color = '#c39797')
colors = sns.color_palette()
plt.xlabel('')
plt.ylabel('')
plt.legend(["Hospitalizuoti", "Nehospitalizuoti"])
plt.title("Ligonių gydymas pagal\n labiausiai paplitusias užkrečiamas ligas")
plt.show()
