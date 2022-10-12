import pandas as pd
import os

specs_path = 'C:/Users/GERARDITO/OneDrive - ASUS/Database/SQL/input/'

specs_asus_path = os.path.join(specs_path, 'specs_asus.xlsx')

df_spec = pd.DataFrame()

def clean_spec_gaming(): 

    specs_gaming = pd.read_excel(specs_asus_path, sheet_name='GAMING NOTEBOOK_Spec')

    df = pd.DataFrame(specs_gaming)

    df['display_original'] = df['Resolution'] + " " + df['Panel Size'] + " " + df['Refresh Rate']
    df['accessories_original'] = df['Bundled Peripherals'] + " " + df['Additional Accessories']
    df['brand_name'] = 'Asus'
    df['business_unit'] = 'Gaming'

    df = df.rename(columns={'Part No':'part_number', 'Model Name':'model_name','BASE UNIT':'base_unit',
                            'Processor':'cpu_original','System Storage Installed':'storage_original',
                            'Total System Memory':'ram_original','Graphic':'gpu_original','Color':'color_original',
                            'Wi-Fi/Bluetooth':'features_original','I/O Ports':'ports_original','Battery':'battery_original',
                            'Weight':'weight_original','Office':'msoffice_original','EAN Code':'EAN','UPC Code':'UPC'})
    
    df.fillna('Not applicable', inplace=True)

    df = df[['part_number', 'model_name', 'base_unit', 'brand_name', 'cpu_original','storage_original',
                'ram_original','display_original','gpu_original','color_original','accessories_original','features_original',
                'ports_original','battery_original','weight_original','msoffice_original','EAN','UPC','business_unit']]

    global df_spec

    df_spec = df

def clean_spec_notebook(): 

    specs_gaming = pd.read_excel(specs_asus_path, sheet_name='NOTEBOOK_Spec')

    df = pd.DataFrame(specs_gaming)

    df['display_original'] = df['Resolution'] + " " + df['Panel Size'] + " " + df['Refresh rate']
    df['accessories_original'] = df['Included in the Box']
    df['brand_name'] = 'Asus'
    df['business_unit'] = 'Notebook'

    df = df.rename(columns={'Part No':'part_number', 'Model Name':'model_name','BASE UNIT':'base_unit',
                            'Processor':'cpu_original','Storage':'storage_original',
                            'Total System Memory':'ram_original','Intergrated GPU':'gpu_original','LCD cover-color':'color_original',
                            'Wireless':'features_original','I/O ports':'ports_original','Battery':'battery_original',
                            'Weight (with Battery)':'weight_original','Office':'msoffice_original','EAN Code':'EAN','UPC Code':'UPC'})
    
    df.fillna('Not applicable', inplace=True)

    df = df[['part_number', 'model_name', 'base_unit', 'brand_name', 'cpu_original','storage_original',
                'ram_original','display_original','gpu_original','color_original','accessories_original','features_original',
                'ports_original','battery_original','weight_original','msoffice_original','EAN','UPC','business_unit']]

    global df_spec

    df_spec = df

def clean_spec_commercial(): 

    specs_gaming = pd.read_excel(specs_asus_path, sheet_name='NOTEBOOK(COMMERCIAL)_Spec')

    df = pd.DataFrame(specs_gaming)

    df['display_original'] = df['Resolution'] + " " + df['Panel Size']
    df['accessories_original'] = df['Included in the Box']
    df['brand_name'] = 'Asus'
    df['business_unit'] = 'Commercial'

    df = df.rename(columns={'Part No':'part_number', 'Model Name':'model_name','BASE UNIT':'base_unit',
                            'Processor':'cpu_original','Storage':'storage_original',
                            'On board memory':'ram_original','Graphics':'gpu_original','LCD cover-color':'color_original',
                            'Wireless':'features_original','I/O ports':'ports_original','Battery':'battery_original',
                            'Weight (with Battery)':'weight_original','Office':'msoffice_original','EAN Code':'EAN','UPC Code':'UPC'})

    df.fillna('Not applicable', inplace=True)

    df = df[['part_number', 'model_name', 'base_unit', 'brand_name', 'cpu_original','storage_original',
                'ram_original','display_original','gpu_original','color_original','accessories_original','features_original',
                'ports_original','battery_original','weight_original','msoffice_original','EAN','UPC','business_unit']]

    global df_spec

    df_spec = df

def clean_spec_aio(): 

    specs_gaming = pd.read_excel(specs_asus_path, sheet_name='ALL IN ONE_Spec')

    df = pd.DataFrame(specs_gaming)

    df['display_original'] = df['Resolution'] + " " + df['Panel Size']
    df['accessories_original'] = df['Included in the box ']
    df['brand_name'] = 'Asus'
    df['business_unit'] = 'All in one'
    df['cpu_original'] = df['On board processor']
    df['ports_original'] = df['Side I/O Port'] + " " + df['Back I/O Port']

    df = df.rename(columns={'Part No':'part_number', 'Model Name':'model_name','BASE UNIT':'base_unit',
                            'Storage':'storage_original',
                            'DIMM Memory':'ram_original','Integrated GPU':'gpu_original','ID Color':'color_original',
                            'Wireless':'features_original','Battery':'battery_original',
                            'Weight':'weight_original','Office':'msoffice_original','EAN Code':'EAN','UPC Code':'UPC'})

    df.fillna('Not applicable', inplace=True)

    df = df[['part_number', 'model_name', 'base_unit', 'brand_name', 'cpu_original','storage_original',
                'ram_original','display_original','gpu_original','color_original','accessories_original','features_original',
                'ports_original','battery_original','weight_original','msoffice_original','EAN','UPC','business_unit']]

    global df_spec

    df_spec = df

print(df_spec)