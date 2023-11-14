import pandas as pd
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
# print(ligu_duombaze.groupby('pranesimo_menuo').size())

# ligu_duombaze[ligu_duombaze["galutine_diagnoze"] =="Vėjaraupiai"]
# print(ligu_duombaze[ligu_duombaze["galutine_diagnoze"] =="Vėjaraupiai"].groupby("pranesimo_menuo").size())

def diagnoziu_kiekis_pagal_menesi(gal_diag):
    return ligu_duombaze[ligu_duombaze["galutine_diagnoze"] == gal_diag].groupby("pranesimo_menuo").size()


print(diagnoziu_kiekis_pagal_menesi("Vėjaraupiai"))