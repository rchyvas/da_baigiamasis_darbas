import requests
import psycopg2
from psycopg2 import sql
import pandas as pd
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
    connection = psycopg2.connect(**conn_params)
    connection.autocommit = True
    cursor = connection.cursor()

    try:
        drop_table_query = sql.SQL("DROP TABLE IF EXISTS {}").format(
            sql.Identifier(table_name)
        )
        cursor.execute(drop_table_query)
        print(f"table '{table_name}' dropped successfully")
    except psycopg2.Error as e:
        print(f"an error occurred while dropping '{table_name}': {e}")

    try:
        columns_with_types = ', '.join([f"{column_name} {data_type}" for column_name, data_type in columns.items()])
        create_table_query = sql.SQL("CREATE TABLE IF NOT EXISTS {} ({})").format(
            sql.Identifier(table_name),
            sql.SQL(columns_with_types)
        )

        cursor.execute(create_table_query)
        print(f"table '{table_name}' created successfully")
    except psycopg2.Error as e:
        print(f"an error occurred while creating '{table_name}: {e}")
    finally:
        cursor.close()
        connection.close()

# create_database(
#     dbname = 'postgres',
#     user = 'postgres',
#     password = 'Y1IOpBVejMxDkNE',
#     host = 'localhost',
#     port = 5432,
#     new_dbname = 'ligos'
# )

conn_params = {
    'dbname': 'ligos',
    'user': 'postgres',
    'password': 'Y1IOpBVejMxDkNE',
    'port': 5432,
    'host': 'localhost'
}

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

# create_table(conn_params, table_name, columns)

def itraukti_ligu_duomenis(conn_params, data):

    connection = psycopg2.connect(**conn_params)
    cursor = connection.cursor()

    insert_stmt = """
    INSERT INTO ligu_duomenys (_id, centras, registravimo_vieta, miestas, galutine_diagnoze, ligonis_hospitalizuotas, socialiai_apdraustas, infekcijos_tipas, is_salies, ligos_klinikine_eiga, atvyk, kreip_diag, pranesimo_menuo, mirtis, sukelejo_rusis)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    index = data.index
    records = data.values.tolist()

    # print("-"*15)

    for i in records:
        cursor.execute(insert_stmt, i)

    connection.commit()

    cursor.close()
    connection.close()
    print("data inserted successfully")

# ligu_duomenys = data_scraping()

# for entry in ligu_duomenys:
#     print(entry)

# itraukti_ligu_duomenis(conn_params, ligu_duomenys)
columns = ['_id', 'centras', 'registravimo_vieta', 'miestas', 'galutine_diagnoze', 'ligonis_hospitalizuotas', 'socialiai_apdraustas', 'infekcijos_tipas', 'is_salies', 'ligos_klinikine_eiga', 'atvyk', 'kreip_diag', 'pranesimo_menuo', 'mirtis', 'sukelejo_rusis']

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

    df = pd.DataFrame(rows)
    df.columns =['_id','centras', 'registravimo_vieta', 'miestas','galutine_diagnoze','ligonis_hospitalizuotas','socialiai_apdraustas','infekcijos_tipas','is_salies','ligos_klinikine_eiga','atvyk','kreip_diag','pranesimo_menuo','mirtis','sukelejo_rusis']

    return df

# table_name = 'ligu_duomenys'
# columns = ['_id', 'centras', 'registravimo_vieta', 'miestas', 'galutine_diagnoze', 'ligonis_hospitalizuotas', 'socialiai_apdraustas', 'infekcijos_tipas', 'is_salies', 'ligos_klinikine_eiga', 'atvyk', 'kreip_diag', 'pranesimo_menuo', 'mirtis', 'sukelejo_rusis']
# conditions = ""
# selected_data = pasirinkti_ligos_duomenis(conn_params, table_name, columns, conditions)
# print(selected_data)

# for row in selected_data:
#     print(row)
