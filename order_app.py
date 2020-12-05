import sqlite3

# Creando base de datos
def create_or_get_database():
    conex = sqlite3.connect('restaurant.db')
    print('BASE DE DATOS CONECTADO CORRECTAMENTE :)')
    return conex

# Metodos para crear las tablas

def create_table_user(conex):
    sql = '''
        CREATE TABLE IF NOT EXISTS user (
            name VARCHAR(100),
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            is_logged INT DEFAULT 0,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    '''
    conex.execute(sql)
    print('Tabla USER creada correctamente')

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

def create_table_order(conex):
    # order es una palabra reservada, marca error, por lo que ocupo ordeer
    sql = '''
        CREATE TABLE IF NOT EXISTS ordeer (
            notes TEXT NOT NULL,
            preparation_time INT NOT NULL,
            total DOUBLE NOT NULL,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES user(rowid)
        )
    '''
    conex.execute(sql)
    print('Tabla ORDER creada correctamente')

# Metodo del menu principal
def principal_menu(conex):
    print('\n')
    print('MENU PRINCIPAL')
    print('1 - Iniciar sesion')
    print('2 - Registrarse')
    print('3 - Salir del programa')
    option = int(input('Ingrese la opcion de lo que quiera realizar: '))
    if validate_user_selection(option, 3):
        selection_principal(option, conex)
    else:
        print('El valor que ingresaste no es valido')
        principal_menu(conex)

# Metodo para llevar a cada opcion del menu principal
def selection_principal(option, conex):
    if option == 1:
        log_in(conex)
    elif option == 2:
        sign_in(conex)
    else:
        pass

# Metodo para iniciar sesion
def log_in(conex):
    email = input('Ingresa tu email: ')
    password = input('Ingresa una contrasena: ')

    try:
        sql = '''
            UPDATE user 
            SET
                is_logged = 1
            WHERE 
                email = ?
            AND 
                password = ?    
        '''
        values = (email, password)
        cursor = conex.execute(sql, values)
        conex.commit

        if cursor.rowcount < 1:
            print('Error al iniciar sesion :(')
        else:
            print('Usuario ha iniciado sesion correctamente')
    except Exception as e:
        print('Algo salio mal durante el inicio de sesion')
        print(e)
        print()

# Metodo para registrarse
def sign_in(conex):
    name = input('Ingresa tu nombre completo: ')
    email = input('Ingresa tu email: ')
    password = input('Ingresa una contrasena: ')
    print()

    sql = '''
        INSERT INTO
        user (name, email, password)
        VALUES (?, ?, ?)
    '''
    values = (name, email, password)
    
    conex.execute(sql, values)
    conex.commit()

    print('>>>>>Usuario creado correctamente!')
    principal_menu(conex)



# Metodo para validar la opcion
def validate_user_selection(option, options):
    return isinstance(option, int) and option > 0 and option <= options

# Metodo principal
def main():
    conex = create_or_get_database()
    create_table_user(conex)
    create_table_dish(conex)
    create_table_order(conex)
    principal_menu(conex)



main()