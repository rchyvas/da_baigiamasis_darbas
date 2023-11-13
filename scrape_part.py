import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

print("Jungiames prie url")
url = "https://get.data.gov.lt/datasets/gov/nvsc/uzkreciamos_ligos/atvejai/Bendrieji"
response = requests.get(url)
print(response)
print('Istraukiam duomenis')
y=response.json()['_data']
ligu_duomenu_lentele = []
print('Sukuriam dataframe')
for entry in y:
    ligu_duomenu_lentele.append([entry['_id'], entry['centras'], entry['registravimo_vieta'], entry['miestas'], entry['galutine_diagnoze'], entry['ligonis_hospitalizuotas'], entry['socialiai_apdraustas'], entry['infekcijos_tipas'], entry['is_salies'], entry['ligos_klinikine_eiga'], entry['atvyk'], entry['kreip_diag'], entry['pranesimo_menuo'], entry['mirtis'], entry['sukelejo_rusis']])
df = pd.DataFrame(ligu_duomenu_lentele)
df.columns =['id','centras', 'registravimo vieta', 'miestas','galutine_diagnoze','ligonis_hospitalizuotas','socialiai_apdraustas','infekcijos_tipas','is_salies','ligos_klinikine_eiga','atvyk','kreip_diag','pranesimo_mienuo','mirtis','sukelejo rusis']

pd.set_option('display.max_columns', 30)  # or 1000
pd.set_option('display.max_rows', 30)  # or 1000
pd.set_option('display.max_colwidth', 30)  # or 199

print(df)