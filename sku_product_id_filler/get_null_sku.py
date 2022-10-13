#I need to connect to DB to get null SKU(product_id)

#Work with tables as dataframes
from cgi import print_directory
from turtle import update
import pandas as pd

#Connect to db
import psycopg2
from sqlalchemy import create_engine

#Work based on folders

import os

#Folder of output dataframe

sku_path = 'C:/Users/GERARDITO/OneDrive - ASUS/Database/SQL/output/'

sku_null_output = os.path.join(sku_path, 'null_sku.xlsx')

#Global df_sku

df_sku = pd.DataFrame()

# Database parameters

connection = psycopg2.connect(
    host='localhost',
    database='asus_db',
    user='postgres',
    password='GitsyLipsy6853',
    port='5432'
)

engine = create_engine('postgresql://postgres:GitsyLipsy6853@localhost:5432/asus_db')

def get_sku_null():

    #Select null product_id from sku table

    sql_select = """ SELECT sku, account_id
                    FROM sku
                    WHERE product_id is null; """

    null_query = pd.read_sql(sql_select, connection)

    df = pd.DataFrame(null_query)

    df['part_number'] = ''

    df.to_excel(sku_null_output)

    print("Nulos obtenidos!")

def read_sku():

    #Read dataframe

    df = pd.read_excel(sku_null_output)

    df['sku'] = df['sku'].apply(lambda x: str(x))

    global df_sku

    df_sku = df

    print("df_sku actualizado!")

    print(df_sku.info())

def update_sku():

    #Create cursor

    psqlCursor = connection.cursor();

    #Delete table if exists so we can be sure before creating new one

    table_name = "temp_sku"

    drop_table_query = """DROP TABLE IF EXISTS %s;"""%table_name

    psqlCursor.execute(drop_table_query)

    connection.commit()

    print("Tabla eliminada!")

    df_sku.to_sql('temp_sku', engine)

    print("Nueva tabla creada!")

    #update_query = """ UPDATE sku
     #                   SET sku.product_id = product_list.id
      #                  FROM sku
       #                 JOIN temp_sku
       #                 ON sku.sku = temp_sku.sku and sku.account_id = temp_sku.account_id
       #                 JOIN product_list
       #                 ON temp_sku.part_number = product_list.part_number"""

    psqlCursor.close();
    connection.close();

read_sku()
update_sku()