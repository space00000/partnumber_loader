#I need to connect to DB to get null SKU(product_id)

#Work with tables as dataframes
import pandas as pd

#Connect to db
import psycopg2

#Work based on folders

import os

#Folder of output dataframe

sku_path = 'C:/Users/GERARDITO/OneDrive - ASUS/Python/'

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

def get_sku_null():

    #Select null product_id from sku table

    sql_select = """ SELECT sku, account_id, product_id
                    FROM sku
                    WHERE product_id is null; """

    null_query = pd.read_sql(sql_select, connection)

    df = pd.DataFrame(null_query)

    df['part_number'] = ''

    df.to_excel(sku_null_output)

def read_sku():

    #Read dataframe

    df = pd.read_excel(sku_null_output)

    global df_sku

    df_sku = df

def update_sku():

    #Create cursor

    psqlCursor = connection.cursor();

    update_query = """ UPDATE sku
                        SET sku.product_id = product_list.id
                        FROM sku
                        JOIN  """