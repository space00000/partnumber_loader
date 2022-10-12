from specs_format_functions import *
from specs_sql import *

def my_menu():
    print()
    print("Explicación: Toma el archivo, le da formato y lo sube a nuestra base de datos.¿")
    print()
    print("Elige la acción que quieres realizar:")
    print()
    print("(1) Limpiar y subir Notebook specs")
    print("(2) Limpiar y subir Gaming specs")
    print("(3) Limpiar y subir Commercial specs")
    print("(4) Limpiar y subir AIO specs")
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
        else:
            print("Favor ingresar un número")
        choice = int(input("Si quieres salir presiona 0 o selecciona otra opción: "))

my_menu()