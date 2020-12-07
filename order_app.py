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
            description TEXT NOT NULL,
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
    print('4 - Eliminar platillo')
    print('5 - Salir del programa')
    option = int(input('Ingrese la opción de lo que quiera realizar: '))
    if validate_user_selection(option):
        selection_principal(option, conex)
    else:
        print('El valor que ingresaste no es valido')
        principal_menu(conex)

# Metodo para llevar a cada opcion del menu principal
def selection_principal(option, conex):
    if option == 1:
        create_dish(conex)
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    else:
        pass

# Metodo para validar la opcion
def validate_user_selection(option):
    return isinstance(option, int) and option > 0 and option <=5

# Metodo para crear un platillo
def create_dish(conex):
    print('--- CREAR PLATILLO ---')
    name = input('Ingresa el nombre: ')
    description = input('Ingresa una descripción: ')
    price = input('Ingresa el precio: ')
    is_available = input('¿Cuántos platillos estan disponibles?: ')

    sql = '''
        INSERT INTO
        dish (name, description, price, is_available)
        VALUES (?, ?, ?, ?)
    '''
    values = (name, description, price, is_available)

    conex.execute(sql, values)
    conex.commit()

    print('Usuario creado correctamete!')
    print('-----------------------------')
    principal_menu(conex)

# Metodo principal
def main():
    conex = create_or_get_database()
    create_table_dish(conex)
    principal_menu(conex)



main()