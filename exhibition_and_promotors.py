import pandas as pd
import os

exhibition_folder = 'C:/Users/GERARDITO/OneDrive - ASUS/Database/SQL/Input'

exhibition_path = os.path.join(exhibition_folder, 'store_promotor.xlsx')

df_ex_total = pd.DataFrame()

def clean_exhibition_totals():

    data = pd.read_excel(exhibition_path)

    df = pd.DataFrame(exhibition_path)

    print(df)

