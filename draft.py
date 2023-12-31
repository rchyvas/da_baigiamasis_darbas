import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# def database():
#     url = "link"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     table = soup.find(table source)
#     column_title = table.find_all('th') #th = table header
#     clean_titles = [title.text.strip() for title in column_title]
#     sub_table = []
#
#     rows = table.find_all('tr') #tr = table row
#     for row in rows:
#         columns = row.find_all('td') #td = table cell
#         player_data - [column.text.strip() for column in columns]
#         sub_table.append(player_data)
#
# df = pd.DataFrame(sub_table, columns = clean_titles)
# print(df)

# def scraping():
#     target = "link"
#     res = requests.get(target) #res = result
#     soup = BeautifulSoup(res.content, 'html.parser')
#     table = soup.find(table source)
#     sub_table = []
#     if table:
#         rows = table.find_all('tr')[1:] #skips the header row
#         for row in rows:
#             cells = row.find_all('td')
#             if len(cells) >= 5 #ensures that there are enough cells
#                 column_title = cells[number].text.strip()
#                 #(...)
#                 sub_table.append([column_title, (...)])
#                 return sub_table

# # from file import scraping data
# data = scraping()
# if data:
#     data = pd.DataFrame(data, columns=['title', (...)])
#     try:
#         print(data)
#     except ValueError as e:
#         print(f"dataframe is empty {e}")
# else:
#     print("no data was scraped")

# import psycopg2
# def create_table(conn_params, table_name, columns):
#     #connection to the database
#     conn = psycopg2.connect(**conn_params)
#     conn.autocommit = True
#     cursor = conn.cursor()
#
#     try:
#         #drop the table if exists
#         drop_table_query = sql.SQL("DROP TABLE IF EXISTS {}").format(
#             sql.Identifier(table_name)
#         )
#         cursor.execute(drop_table_query)
#         print(f"table '{table_name}' dropped successfully")
#     except psycopg2.Error as e:
#         print(f"an error occurred while dropping '{table_name}': {e}")
#
#     try:
#         #define the create table query
#         columns_with_types = ','.join([f"{column_name}{data_type}" for column_name, data_type in columns.items()])
#         create_table_query = sql.SQL("CREATE TABLE IF NOT EXISTS {} ({})").format(
#             sql.Identifier(table_name),
#             sql.SQL(columns_with_types)
#         )
#
#         #execute the create table query
#         cursor.execute(create_table_query)
#         print(f"table '{table_name}' created successfully")
#     except psycopg2.Error as e:
#         print(f"an error occurred while creating '{table_name}: {e}")
#     finally:
#         #close the cursor and the connection
#         cursor.close()
#         conn.close()

# import psycopg2
# from psycopg2 import sql
# from currency_scraper import currency_scraping
#
#
# def connect_db():
#     conn_params = {
#         'dbname': 'valiutos',
#         'user': 'postgres',
#         'password': '123456',
#         'host': 'localhost'
#     }
#     return conn_params
#
#
# def create_database(dbname, user, password, host, port, new_dbname):
#     # Connection string
#     conn_params = {
#         'dbname': dbname,
#         'user': user,
#         'password': password,
#         'host': host
#     }
#
#     # Establish a connection to the database
#     try:
#         # Connect to the PostgreSQL server
#         conn = psycopg2.connect(**conn_params)
#         conn.autocommit = True  # this is necessary for database creation
#
#         # Create a cursor object
#         cur = conn.cursor()
#
#         # Execute the database creation command
#         cur.execute(sql.SQL("CREATE DATABASE{}").format(sql.Identifier(new_dbname)))
#
#         print(f"Database {new_dbname} created successfully.")
#
#         # Close the cursor and connection
#         cur.close()
#         conn.close()
#
#     except psycopg2.Error as e:
#         print(f"An error occurred while creating the database: {e}")
#
#
# # create_database(
# #     dbname='postgres',
# #     user='postgres',
# #     password='123456',
# #     host='localhost',
# #     port=5432,
# #     new_dbname='valiutos'
# # )
#
# def create_table(conn_params, table_name, columns):
#     # Connect to the database
#     conn = psycopg2.connect(**conn_params)
#     conn.autocommit = True
#     cursor = conn.cursor()
#
#     try:
#         # Drop the table if it exists
#         drop_table_query = sql.SQL("DROP TABLE IF EXISTS {}").format(
#             sql.Identifier(table_name)
#         )
#         cursor.execute(drop_table_query)
#         print(f"Table {table_name} dropped successfully!")
#     except psycopg2.Error as e:
#         print(f"An error occurred while dropping {table_name}: {e}")
#
#     try:
#         # Define the create table query
#         columns_with_types = ', '.join([f"{col_name} {data_type}" for col_name, data_type in columns.items()])
#         create_table_query = sql.SQL("CREATE TABLE IF NOT EXISTS {} ({})").format(
#             sql.Identifier(table_name),
#             sql.SQL(columns_with_types)
#         )
#
#         # Execute the create table query
#         cursor.execute(create_table_query)
#         print(f"Table {table_name} created successfully.")
#     except psycopg2.Error as e:
#         print(f"An error occurred while creating {table_name}: {e}")
#     finally:
#         # Close the cursor and the connection
#         cursor.close()
#         conn.close()
#
#
# # Connection parameters
# conn_params = {
#     'dbname': 'valiutos',
#     'user': 'postgres',
#     'password': '123456',
#     'host': 'localhost'
# }
#
# # Table details
# table_name = 'currency_rates'
# columns = {
#     'id': 'SERIAL PRIMARY KEY',
#     'title': 'VARCHAR(100)',
#     'currency_code': 'VARCHAR(10)',
#     'curr_proportion': 'DECIMAL(10,2)',
#     'curr_change': 'DECIMAL(10,2)',
#     'curr_change_percentage': 'DECIMAL(10,2)',
#     'currency_date': 'DATE'
# }
#
#
# # Create table
# # create_table(conn_params, table_name, columns)
#
# def insert_currency_data(conn_params, data):
#     # Establish a connection to the database
#     conn = psycopg2.connect(**conn_params)
#     cur = conn.cursor()
#
#     insert_stmt = """
#     INSERT INTO currency_rates (currency_date, title, currency_code, curr_proportion, curr_change, curr_change_percentage)
#     VALUES (%s, %s, %s, %s, %s, %s)
#     """
#
#     for row in data:
#         cur.execute(insert_stmt, row)
#
#     conn.commit()
#
#     cur.close()
#     conn.close()
#     print("Data inserted successfully.")
#
#
# currency_data = currency_scraping()
#
# # insert_currency_data(conn_params, currency_data)
#
# columns = ['currency_date','title', 'currency_code', 'curr_proportion', 'curr_change', 'curr_change_percentage']
#
#
# def select_currency_data(conn_params, table_name, columns=columns, conditions=None):
#     conn = psycopg2.connect(**conn_params)
#     cur = conn.cursor()
#
#     select_stmt = f"SELECT {columns} from {table_name} "
#
#     if isinstance(columns, list):
#         columns = ', '.join(columns)
#         select_stmt = f"SELECT {columns} from {table_name} "
#
#     if conditions:
#         select_stmt += f"WHERE {conditions}"
#
#     cur.execute(select_stmt)
#     rows = cur.fetchall()
#
#     cur.close()
#     conn.close()
#
#     return rows
#
# # table_name = 'currency_rates'
# # columns = ['title', 'currency_rate', 'curr_proportion', 'curr_change', 'curr_change_percentage']
# # conditions = ""
# # selected_data = select_currency_data(conn_params, table_name, columns, conditions)
# #
# # for row in selected_data:
# #     print(row)

# fig, ax = plt.subplots()
#
# fruits = ['apple', 'blueberry', 'cherry', 'orange']
# counts = [40, 100, 30, 55]
# bar_labels = ['red', 'blue', '_red', 'orange']
# bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
#
# ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
#
# ax.set_ylabel('fruit supply')
# ax.set_title('Fruit supply by kind and color')
# ax.legend(title='Fruit color')
#
# plt.show()

# # Data for plotting
# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2 * np.pi * t)
#
# fig, ax = plt.subplots()
# ax.plot(t, s)
#
# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#         title='About as simple as it gets, folks')
# ax.grid()
#
# fig.savefig("test.png")
# plt.show()

# t = np.linspace(0, 2 * np.pi, 1024)
# data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :]
#
# fig, ax = plt.subplots()
# im = ax.imshow(data2d)
# ax.set_title('Pan on the colorbar to shift the color mapping\n'
#              'Zoom on the colorbar to scale the color mapping')
#
# fig.colorbar(im, ax=ax, label='Interactive colorbar')
#
# plt.show()

# # Create some mock data
# t = np.arange(0.01, 10.0, 0.01)
# data1 = np.exp(t)
# data2 = np.sin(2 * np.pi * t)
#
# fig, ax1 = plt.subplots()
#
# color = 'tab:red'
# ax1.set_xlabel('time (s)')
# ax1.set_ylabel('exp', color=color)
# ax1.plot(t, data1, color=color)
# ax1.tick_params(axis='y', labelcolor=color)
#
# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
#
# color = 'tab:blue'
# ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
# ax2.plot(t, data2, color=color)
# ax2.tick_params(axis='y', labelcolor=color)
#
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.show()
