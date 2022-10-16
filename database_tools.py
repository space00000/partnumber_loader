from specs_format_functions import *
from specs_sql import *
from sku_product_id_filler.get_null_sku import *

def my_menu():
    print()
    print("Conjunto de herramientas para mantener la DB Actualizada")
    print()
    print("Elige la acción que quieres realizar:")
    print()
    print("(1) Limpiar y subir Notebook specs")
    print("(2) Limpiar y subir Gaming specs")
    print("(3) Limpiar y subir Commercial specs")
    print("(4) Limpiar y subir AIO specs")
    print("(5) Obtener sku sin part-number")
    print("(6) Actualizar part-number de sku")
    print("(0) Salir")
    print()
    choice = int(input("Ingresa tu opción: "))
    print()

    while (choice != 0):
        if choice == 1:
            clean_spec_notebook()
            upload()
        elif choice == 2:
            clean_spec_gaming()
            upload()
        elif choice == 3:
            clean_spec_commercial()
            upload()
        elif choice == 4:
            clean_spec_aio()
            upload()
        elif choice == 5:
            get_sku_null()
        elif choice == 6:
            read_sku()
            update_sku()
        else:
            print("Favor ingresar un número")
        choice = int(input("Si quieres salir presiona 0 o selecciona otra opción: "))

my_menu()