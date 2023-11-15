import requests
import pandas as pd
import json


def data_scraping():

    print("prisijungimas prie svetainės")
    url = "https://get.data.gov.lt/datasets/gov/nvsc/uzkreciamos_ligos/atvejai/Bendrieji"
    response = requests.get(url)
    print(response)
    print('duomenų surinkimas')
    y=response.json()['_data']
    ligu_duomenu_lentele = []
    print('dataframe kūrimas')
    for entry in y:
        ligu_duomenu_lentele.append([entry['_id'], entry['centras'], entry['registravimo_vieta'], entry['miestas'], entry['galutine_diagnoze'].strip(), entry['ligonis_hospitalizuotas'], entry['socialiai_apdraustas'], entry['infekcijos_tipas'], entry['is_salies'], entry['ligos_klinikine_eiga'], entry['atvyk'], entry['kreip_diag'], entry['pranesimo_menuo'], entry['mirtis'], entry['sukelejo_rusis']])
    df = pd.DataFrame(ligu_duomenu_lentele)
    df.columns =['_id','centras', 'registravimo_vieta', 'miestas','galutine_diagnoze','ligonis_hospitalizuotas','socialiai_apdraustas','infekcijos_tipas','is_salies','ligos_klinikine_eiga','atvyk','kreip_diag','pranesimo_menuo','mirtis','sukelejo_rusis']

    # pd.set_option('display.max_columns', 30)  # or 1000
    # pd.set_option('display.max_rows', 30)  # or 1000
    # pd.set_option('display.max_colwidth', 30)  # or 199

    return df

# print(data_scraping())
