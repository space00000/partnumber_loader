

from cmath import nan
from datetime import datetime, timedelta
import datetime
from tokenize import blank_re
import pandas as pd
import os
import numpy as np

customer_id_function = lambda row: 1 if row.customer_name == 'Falabella' else \
     (4 if row.customer_name == 'Ripley' else \
        (3 if row.customer_name == 'Paris' else 0))

barcode_rules = lambda row: row.Barcode + '999' if row.Barcode_count == 6 and row.customer_id == 3 \
                                  else (row.Barcode[2:11] if row.Barcode[0:2] == '20' and row.customer_id == 3 \
                                    else (row.Barcode[4:12] if row.customer_id == 4 \
                                        else row.Barcode))

exhibition_folder = 'C:/Users/GERARDITO/OneDrive - ASUS/Python/exhibition_cleaner/'

exhibition_path = os.path.join(exhibition_folder, 'retail_exhibition.xlsx')

exhibition_output = os.path.join(exhibition_folder, 'test1.xlsx')

df_exhibition = pd.DataFrame()

def clean_exhibition():

  f_data = pd.read_excel(exhibition_path)

  df = pd.DataFrame(f_data)

  df.drop_duplicates()

  df = df.rename(columns={'Sheet Name':'customer_name'})

  df["Barcode"] = df["Barcode"].astype(str)

  df = df[~df['Barcode'].str.contains('http')]

  df['customer_id'] = df.apply(customer_id_function, axis = 1)

  df['Location'].str.split(',', expand=True)

  df[['Latitude', 'Longitude']] = df['Location'].str.split(',', expand=True)

  df['Barcode_count'] = df['Barcode'].str.len()

  df['Barcode_rules'] = df.apply(barcode_rules, axis=1)

  df = df[df['Longitude'].notnull()]

  df = df[df['Barcode_rules'] != '15320-00230000']

  df["Latitude"] = pd.to_numeric(df["Latitude"], errors= 'coerce')

  df["Longitude"] = pd.to_numeric(df["Longitude"], errors= 'coerce')

  df["Latitude"] = df["Latitude"].round(decimals=2)

  df["Longitude"] = df["Longitude"].round(decimals=2)

  df = df[["Date",
          "customer_name",
          "customer_id",
          "Barcode_rules",
          "Latitude",
          "Longitude"]]

  df = df.drop_duplicates()

  #Dates

  df['Date'] = pd.to_datetime(df['Date'])

  today = datetime.date.today()

  last_week_monday = today - timedelta(days=today.weekday()) + timedelta(days=0, weeks=-1)

  pd_lw = pd.Timestamp(last_week_monday)

  mask = (df['Date'] > pd_lw)

  df['Date'] = pd.to_datetime(df['Date']).dt.date

  global df_exhibition

  df_exhibition = df.loc[mask]

