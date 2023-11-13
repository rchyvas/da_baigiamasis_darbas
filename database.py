import requests
from bs4 import BeautifulSoup
import psycopg2
from psycopg2 import sql
import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import json
# import urllib.request
from skreipinimas import data_scraping

def connect_db():
    conn_params = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'Y1IOpBVejMxDkNE',
        'host': 'localhost'
    }
    return conn_params
def create_database(dbname, user, password, host, port, new_dbname):
    # connection string
    conn_params = {
        'dbname': dbname,
        'user': user,
        'password': password,
        'port': port,
        'host': host
    }
    try:
        connection = psycopg2.connect(**conn_params)
        connection.autocommit = True

        cursor = connection.cursor()

        cursor.execute(sql.SQL("CREATE DATABASE{}").format(sql.Identifier(new_dbname)))
        print(f"database '{new_dbname}' created successfully")

        cursor.close()
        connection.close()

    except psycopg2.Error as e:
        print(f"an error occurred while creating database: {e}")


def create_table(conn_params, table_name, columns):
    #connection to the database
    connection = psycopg2.connect(**conn_params)
    connection.autocommit = True
    cursor = connection.cursor()

    try:
        #drop the table if exists
        drop_table_query = sql.SQL("DROP TABLE IF EXISTS {}").format(
            sql.Identifier(table_name)
        )
        cursor.execute(drop_table_query)
        print(f"table '{table_name}' dropped successfully")
    except psycopg2.Error as e:
        print(f"an error occurred while dropping '{table_name}': {e}")

    try:
        #define the create table query
        columns_with_types = ', '.join([f"{column_name}{data_type}" for column_name, data_type in columns.items()])
        create_table_query = sql.SQL("CREATE TABLE IF NOT EXISTS ligu_duomenys (id serial PRIMARY KEY, _id VARCHAR(300), centras VARCHAR(300), registravimo_vieta VARCHAR(300), miestas VARCHAR(300), galutine_diagnoze VARCHAR(500), ligonis_hospitalizuotas BOOLEAN, socialiai_apdraustas BOOLEAN, infekcijos_tipas VARCHAR(300),is_salies VARCHAR(300), ligos_klinikine_eiga VARCHAR(300), atvyk VARCHAR(300), kreip_diag INTEGER, pranesimo_menuo DATE, mirtis BOOLEAN, sukelejo_rusis VARCHAR(300))")
        # create_table_query = sql.SQL("CREATE TABLE IF NOT EXISTS {} ({})").format(
        #     sql.Identifier(table_name),
        #     sql.SQL(columns_with_types)
        # )

        #execute the create table query
        cursor.execute(create_table_query)
        print(f"table '{table_name}' created successfully")
    except psycopg2.Error as e:
        print(f"an error occurred while creating '{table_name}: {e}")
    finally:
        #close the cursor and the connection
        cursor.close()
        connection.close()

create_database(
    dbname = 'postgres',
    user = 'postgres',
    password = 'Y1IOpBVejMxDkNE',
    host = 'localhost',
    port = 5432,
    new_dbname = 'ligos'
)

# connection parameters
conn_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'Y1IOpBVejMxDkNE',
    'port': 5432,
    'host': 'localhost'
}

# table details
table_name = 'ligu_duomenys'
columns = {
    'id': 'serial PRIMARY KEY',
    '_id': 'VARCHAR(300)',
    'centras': 'VARCHAR(300)',
    'registravimo_vieta': 'VARCHAR(300)',
    'miestas': 'VARCHAR(300)',
    'galutine_diagnoze': 'VARCHAR(500)',
    'ligonis_hospitalizuotas': 'BOOLEAN',
    'socialiai_apdraustas': 'BOOLEAN',
    'infekcijos_tipas': 'VARCHAR(300)',
    'is_salies': 'VARCHAR(300)',
    'ligos_klinikine_eiga': 'VARCHAR(300)',
    'atvyk': 'VARCHAR(300)',
    'kreip_diag': 'INTEGER',
    'pranesimo_menuo': 'DATE',
    'mirtis': 'BOOLEAN',
    'sukelejo_rusis': 'VARCHAR(300)'
}

# create table
create_table(conn_params, table_name, columns)

def itraukti_ligu_duomenis(conn_params, data):
    # establish a connection to the database

    print("funkcija pradeda veikti")

    connection = psycopg2.connect(**conn_params)
    # print(connection)
    cursor = connection.cursor()
    # print(cursor)

    insert_stmt = """
    INSERT INTO ligu_duomenys (id, _id, centras, registravimo_vieta, miestas, galutine_diagnoze, ligonis_hospitalizuotas, socialiai_apdraustas, infekcijos_tipas, is_salies, ligos_klinikine_eiga, atvyk, kreip_diag, pranesimo_menuo, mirtis, sukelejo_rusis)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    # print(insert_stmt)
    # print(data)
    # for row in data:
        # print(row)

    index = data.index
    # print(index)
    records = list(data.to_records(index = False))

    # print(data.iloc[0])
    print("-"*15)

    # for i in records:
    #     print(i)
    #     print("-" * 15)
    cursor.execute(insert_stmt, (1, 'f7c8ef64-b4e5-4fe6-98ca-6f6537f543b3', 'Kaunas', 'Kaunas', 'Kaunas', 'Apatinių lytinių ir šlapimo takų chlamidijų sukelta infekcija', False, True, 'ūmi liga', None, None, float("nan"), 136, '2023-01-01', None, '|Chlamydia trachomatis|'))

    connection.commit()

    cursor.close()
    connection.close()
    print("data inserted successfully")

ligu_duomenys = data_scraping()
print(type(ligu_duomenys))

print("ligų duomenų tikrinimas prieš funkcijos patikrinimą")
for entry in ligu_duomenys:
    print(entry)
print("kviečiam duomenų įtraukimo funkciją")
itraukti_ligu_duomenis(conn_params, ligu_duomenys)
columns = ['id', '_id', 'centras', 'registravimo_vieta', 'miestas', 'galutine_diagnoze', 'ligonis_hospitalizuotas', 'socialiai_apdraustas', 'infekcijos_tipas', 'is_salies', 'ligos_klinikine_eiga', 'atvyk', 'kreip_diag', 'pranesimo_menuo', 'mirtis', 'sukelejo_rusis']

def pasirinkti_ligos_duomenis(conn_params, table_name, columns=columns, conditions = None):
    connection = psycopg2.connect(**conn_params)
    cursor = connection.cursor()

    select_stmt = f"SELECT {columns} from {table_name}"

    if isinstance(columns,list):
        columns = ','.join(columns)
        select_stmt = f"SELECT {columns} from {table_name}"

    if conditions:
        select_stmt += f"WHERE {conditions}"

    cursor.execute(select_stmt)
    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows

table_name = 'ligu_duomenys'
columns = ['id', '_id', 'centras', 'registravimo_vieta', 'miestas', 'galutine_diagnoze', 'ligonis_hospitalizuotas', 'socialiai_apdraustas', 'infekcijos_tipas', 'is_salies', 'ligos_klinikine_eiga', 'atvyk', 'kreip_diag', 'pranesimo_menuo', 'mirtis', 'sukelejo_rusis']
conditions = ""
selected_data = pasirinkti_ligos_duomenis(conn_params, table_name, columns, conditions)

for row in selected_data:
    print(row)