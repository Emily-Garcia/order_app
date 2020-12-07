# -- coding: utf-8 --

import sqlite3

# Creando base de datos
def create_or_get_database():
    conex = sqlite3.connect('restaurant.db')
    print('BASE DE DATOS CONECTADO CORRECTAMENTE :)')
    return conex

# Métodos para crear las tablas
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

# Método del menu principal
def principal_menu(conex):
    print('MENÚ')
    print('1 - Crear platillo')
    print('2 - Ver platillos')
    print('3 - Actualizar platillo')
    print('4 - Eliminar platillo')
    print('5 - Salir del programa')
    option = int(input('Ingrese la opción de lo que quiera realizar: '))
    if validate_user_selection(option):
        selection_principal(option, conex)
    else:
        print('El valor que ingresaste no es válido')
        principal_menu(conex)

# Método para llevar a cada opcion del menu principal
def selection_principal(option, conex):
    if option == 1:
        create_dish(conex)
    elif option == 2:
        see_dishes(conex)
    elif option == 3:
        update_dish(conex)
    elif option == 4:
        delete_dish(conex)
    else:
        pass

# Método para validar la opcion
def validate_user_selection(option):
    return isinstance(option, int) and option > 0 and option <=5

# Método para crear un platillo
def create_dish(conex):
    print()
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

    print('PLATILLO CREADO!')
    print('-----------------------------')
    principal_menu(conex)

# Método para ver los platillos
def see_dishes(conex):
    print()
    print('--- VER PLATILLOS ----')
    sql = '''
    SELECT
        rowid, name, description, price, is_available, timestamp
    FROM
        dish
    '''
    cursor = conex.execute(sql)

    for row in cursor:
        print('* * *')
        print(f'ID: {row[0]}')
        print(f'Nombre: {row[1]}')
        print(f'Descripción: {row[2]}')
        print(f'Precio: {row[3]}')
        print(f'Platillos disponibles: {row[4]}')
        print(f'Última actualización: {row[5]}')

    print('-------------------------')
    principal_menu(conex)

# Método para actualizar un platillo
def update_dish(conex):
    print()
    print('--- ACTUALIZAR PLATILLO ---')
    rowid = input('Ingresa el ID del platilo: ')
    print('Columnas:')
    print('1. Nombre')
    print('2. Descripción')
    print('3. Precio')
    print('4. Platillos disponibles')
    num_column = int( input('Ingresa el número de la columna que quieres actualizar: '))
    if num_column == 1:
        column = 'name'
    elif num_column == 2:
        column = 'description'
    elif num_column == 3:
        column = 'price'
    elif num_column == 4:
        column = 'is_available'
    else:
        print('>>> La opción que ingresaste no es válido, ingresa de nuevo los datos.<<<')
        update_dish(conex)

    new_value = input('Ingresa el nuevo valor de dicha columna: ')

    try:
        sql = f'''
            UPDATE dish
            SET
                {column} = ?
            WHERE
                rowid = ?
        '''
        values = (new_value, rowid)
        cursor = conex.execute(sql, values)
        conex.commit()

        if cursor.rowcount < 1:
            print('No se actualizó el platillo correctamente')
        else:
            print('PLATILLO ACTUALIZADO!')
    except Exception as e:
        print('Ocurrio un error durante la actualización')
        print(e)
    print('--------------------------------')
    principal_menu(conex)

# Método para eliminar platillo
def delete_dish(conex):
    print()
    print('--- ELIMINAR PLATILLO ---')
    rowid = input('Ingrese el ID del platillo: ')

    try:
        sql = '''
            DELETE FROM dish
            WHERE
                rowid = ?
        '''
        values = (rowid)
        conex.execute(sql, values)
        conex.commit()
        print('PLATILLO ELIMINADO')
    except Exception as e:
        print('Hubo un error al eliminar el platillo.')
        print(e)
    print('----------------------------')
    principal_menu(conex)

# Método principal
def main():
    conex = create_or_get_database()
    create_table_dish(conex)
    principal_menu(conex)



main()