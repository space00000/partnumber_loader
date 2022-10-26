#Modules and connection

import specs_format_functions
from specs_format_functions import *
from sqlalchemy import create_engine
from sqlite3 import connect
import psycopg2
import exhibition_cleaner
from exhibition_cleaner import *

#Open datatbase connection with psycopg2

connection = psycopg2.connect(
    host='localhost',
    database='asus_db',
    user='postgres',
    password='GitsyLipsy6853',
    port='5432'
)

#Create database engine to work with

engine = create_engine('postgresql://postgres:GitsyLipsy6853@localhost:5432/asus_db')

#Crear SQL script para subir datos

def upload():

    #Siempre abrir cursos para poder trabajar

    psqlCursor = connection.cursor();

    #Borrar tabla si es que existe, asi evitamos duplicacion

    tableName = "temp_specs";

    dropTableStmt = "DROP TABLE IF EXISTS %s;"%tableName;

    psqlCursor.execute(dropTableStmt);

    connection.commit()

    #Crear tabla a partir del df creado por las funciones de formateo

    specs_format_functions.df_spec.to_sql('temp_specs', engine)

    #Insertar cada uno de los specs a sus tablas, asi me aseguro que existe un id antes de subir a product_list

    insert_brand = """INSERT INTO product_brand (brand_name)
                    select distinct n.brand_name
                    FROM temp_specs n
                    WHERE NOT EXISTS (SELECT 1
                    FROM product_brand c
                    WHERE c.brand_name = n.brand_name);"""

    psqlCursor.execute(insert_brand);
    connection.commit()

    insert_cpu = """INSERT INTO product_cpu (cpu_original)
                    select distinct n.cpu_original
                    FROM temp_specs n
                    WHERE NOT EXISTS (SELECT 1
                    FROM product_cpu c 
                    WHERE c.cpu_original = n.cpu_original);"""

    psqlCursor.execute(insert_cpu);
    connection.commit()

    insert_storage = """INSERT INTO product_storage (storage_original)
                    select distinct n.storage_original 
                    FROM temp_specs n
                    WHERE NOT EXISTS (SELECT 1
                    FROM product_storage c 
                    WHERE c.storage_original  = n.storage_original);"""

    psqlCursor.execute(insert_storage);
    connection.commit()

    insert_ram = """INSERT INTO product_ram (ram_original)
                    select distinct n.ram_original
                    FROM temp_specs n
                    WHERE NOT EXISTS (SELECT 1
                    FROM product_ram c 
                    WHERE c.ram_original = n.ram_original);"""

    psqlCursor.execute(insert_ram);
    connection.commit()

    insert_display = """INSERT INTO product_display (display_original)
                    select distinct n.display_original
                    FROM temp_specs n
                    WHERE NOT EXISTS (SELECT 1
                    FROM product_display c 
                    WHERE c.display_original = n.display_original);"""

    psqlCursor.execute(insert_display);
    connection.commit()

    insert_gpu = """INSERT INTO product_gpu (gpu_original)
                    select distinct n.gpu_original
                    FROM temp_specs n
                    WHERE NOT EXISTS (SELECT 1
                    FROM product_gpu c 
                    WHERE c.gpu_original  = n.gpu_original);"""

    psqlCursor.execute(insert_gpu);
    connection.commit()

    insert_color = """INSERT INTO product_color (color_original)
                    select distinct n.color_original  
                    FROM temp_specs n
                    WHERE NOT EXISTS (SELECT 1
                    FROM product_color c 
                    WHERE c.color_original = n.color_original);"""

    psqlCursor.execute(insert_color);
    connection.commit()

    insert_accessories = """INSERT INTO product_accessories (accessories_original)
                    select distinct n.accessories_original
                    FROM temp_specs n
                    WHERE NOT EXISTS (SELECT 1
                    FROM product_accessories c 
                    WHERE c.accessories_original = n.accessories_original);"""

    psqlCursor.execute(insert_accessories);
    connection.commit()

    insert_features = """INSERT INTO product_features (features_original)
                    select distinct n.features_original 
                    FROM temp_specs n
                    WHERE NOT EXISTS (SELECT 1
                    FROM product_features c 
                    WHERE c.features_original = n.features_original);"""

    psqlCursor.execute(insert_features);
    connection.commit()

    insert_ports = """INSERT INTO product_ports (ports_original)
                    select distinct n.ports_original
                    FROM temp_specs n
                    WHERE NOT EXISTS (SELECT 1
                    FROM product_ports c 
                    WHERE c.ports_original = n.ports_original);"""

    psqlCursor.execute(insert_ports);
    connection.commit()

    insert_battery = """INSERT INTO product_battery (battery_original)
                    select distinct n.battery_original
                    FROM temp_specs n
                    WHERE NOT EXISTS (SELECT 1
                    FROM product_battery c 
                    WHERE c.battery_original = n.battery_original);"""

    psqlCursor.execute(insert_battery);
    connection.commit()

    insert_weight = """INSERT INTO product_weight (weight_original)
                    select distinct n.weight_original
                    FROM temp_specs n
                    WHERE NOT EXISTS (SELECT 1
                    FROM product_weight c 
                    WHERE c.weight_original = n.weight_original);"""

    psqlCursor.execute(insert_weight);
    connection.commit()

    insert_office = """INSERT INTO product_msoffice (msoffice_original)
                    select distinct n.msoffice_original
                    FROM temp_specs n
                    WHERE NOT EXISTS (SELECT 1
                    FROM product_msoffice c 
                    WHERE c.msoffice_original = n.msoffice_original);"""

    psqlCursor.execute(insert_office);
    connection.commit()

    insert_business = """INSERT INTO business_unit (business_unit)
                    select distinct n.business_unit
                    FROM temp_specs n
                    WHERE NOT EXISTS (SELECT 1
                    FROM business_unit c 
                    WHERE c.business_unit = n.business_unit);"""

    psqlCursor.execute(insert_business);
    connection.commit()


    insert_table = """insert into product_list (part_number, model_name, base_unit,
                            brand_id, cpu_id, storage_id, ram_id, display_id, gpu_id, color_id,
                            accessories_id, features_id, product_ports_id, battery_id, weight_id,
                            ms_office_id, "EAN", business_unit_id, "UPC")
                            select tabla.part_number, tabla.model_name , tabla.base_unit,
                            brand.id, cpu.id, psto.id, pram.id, pdis.id, pgpu.id, pcolor.id,
                            pacc.id, pfea.id, ppo.id, pbat.id, pwe.id,
                            pmso.id, tabla.EAN, bu.id, tabla.UPC
                            from temp_specs tabla
                            left join product_brand brand
                            on tabla.brand_name  = brand.brand_name
                            left join product_cpu cpu
                            on tabla.cpu_original  = cpu.cpu_original
                            left join product_storage psto
                            on tabla.storage_original  = psto.storage_original 
                            left join product_ram pram
                            on tabla.ram_original  = pram.ram_original 
                            left join product_display pdis
                            on tabla.display_original  = pdis.display_original 
                            left join product_gpu pgpu
                            on tabla.gpu_original  = pgpu.gpu_original
                            left join product_color pcolor
                            on tabla.color_original = pcolor.color_original 
                            left join product_accessories pacc
                            on tabla.accesories_original  = pacc.accessories_original 
                            left join product_features pfea
                            on tabla.features_original  = pfea.features_original 
                            left join product_ports ppo
                            on tabla.ports_original  = ppo.ports_original 
                            left join product_battery pbat
                            on tabla.battery_original = pbat.battery_original 
                            left join product_weight pwe
                            on tabla.weight_original = pwe.weight_original 
                            left join product_msoffice pmso
                            on tabla.msoffice_original  = pmso.msoffice_original 
                            left join business_unit bu
                            on tabla.business_unit  = bu.business_unit ;"""

    psqlCursor.execute(insert_table);
    connection.commit()

    print('Datos subidos!')

    #End connection to database

    psqlCursor.close();

    connection.close();

def upload_exhibition():

    #Siempre abrir cursos para poder trabajar

    psqlCursor = connection.cursor();

    #Borrar tabla si es que existe, asi evitamos duplicacion

    tableName = "temp_exhibition";

    dropTableStmt = "DROP TABLE IF EXISTS %s;"%tableName;

    psqlCursor.execute(dropTableStmt);

    connection.commit()

    #Crear tabla a partir del df creado por las funciones de formateo

    exhibition_cleaner.df_exhibition.to_sql('temp_exhibition', engine)

    insert_table = """INSERT INTO store_exhibition(exhibition_date, barcode, latitude, longitude, account_id)
                        SELECT tx."Date", tx."Barcode_rules", tx."Latitude", tx."Longitude", tx."customer_id"
                        FROM temp_exhibition tx """

    psqlCursor.execute(insert_table);
    connection.commit()

    update_product_id_ean = """update store_exhibition st
                                set product_id = pl.id
                                from product_list pl
                                where pl."EAN" = st."barcode";"""

    psqlCursor.execute(update_product_id_ean);
    connection.commit()

    update_product_id_sku = """update store_exhibition st
                                set product_id = sk.product_id
                                from sku sk
                                where sk.sku = st."barcode"
                                and sk.account_id = st.account_id ;"""

    psqlCursor.execute(update_product_id_sku);
    connection.commit()

    update_store_id = """update store_exhibition st
                            set store_id = ss.id 
                            from store ss
                        where ss.account_id = st.account_id 
                        and ss.latitude_short = st."latitude" 
                        and ss.longitude_short = st."longitude" ;"""

    psqlCursor.execute(update_store_id);
    connection.commit()

    print('Datos subidos!')

    #End connection to database

    psqlCursor.close();

    connection.close();
