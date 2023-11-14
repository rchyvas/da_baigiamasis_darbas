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

