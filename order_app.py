# -- coding: utf-8 --

import sqlite3

# Creando base de datos
def create_or_get_database():
    conex = sqlite3.connect('restaurant.db')
    print('BASE DE DATOS CONECTADO CORRECTAMENTE :)')
    return conex

# Metodos para crear las tablas
def create_table_dish(conex):
    sql = '''
        CREATE TABLE IF NOT EXISTS dish (
            name VARCHAR NOT NULL,
            descripcion TEXT NOT NULL,
            price DOUBLE NOT NULL,
            is_available INT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    '''
    conex.execute(sql)
    print('Tabla DISH creada correctamente')

# Metodo del menu principal
def principal_menu(conex):
    print('\n')
    print('MENU')
    print('1 - Crear platillo')
    print('2 - Ver platillos')
    print('3 - Actualizar platillo')
    print('3 - Eliminar platillo')
    option = int(input('Ingrese la opcion de lo que quiera realizar: '))
    if validate_user_selection(option, 3):
        selection_principal(option, conex)
    else:
        print('El valor que ingresaste no es valido')
        principal_menu(conex)

# Metodo para llevar a cada opcion del menu principal
def selection_principal(option, conex):
    if option == 1:
        pass
    elif option == 2:
        pass
    else:
        pass

# Metodo para validar la opcion
def validate_user_selection(option, options):
    return isinstance(option, int) and option > 0 and option <= options

# Metodo principal
def main():
    conex = create_or_get_database()
    create_table_dish(conex)
    principal_menu(conex)



main()