import requests
from bs4 import BeautifulSoup
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

url = "https://get.data.gov.lt/datasets/gov/nvsc/uzkreciamos_ligos/atvejai/Bendrieji"
response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")