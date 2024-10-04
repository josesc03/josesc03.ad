########################################
# UNIDAD 2 - Ejercicio obligatorio     #
# Credenciales de jugadores (ESQUEMA)  #
########################################
import sqlite3

# DEFINICIÓN DE FUNCIONES --------------------------------------
def valida_opcion():
    """Función que muestra un menú y valida que la opción sea correcta"""

    opc_correctas = ['1', '2', '3', '4', '5', '0']
    
    #Mostramos el menú y solicitamos la operación al usuario
    opcion = ''
    while opcion not in opc_correctas:
        print()
        print("==================================")            
        print("     CREDENCIALES JUGADORES       ")
        print("==================================")
        print(" 1 - Imprimir jugadores")
        print(" 2 - Validar credencial ")       
        print(" 3 - Cambiar credencial ")
        print(" 4 - Insertar nuevo jugador ")
        print(" 5 - Borrar jugador ")
        print(" 0 - SALIR ")
        print("--------------------------")    
        opcion = input("Dame la opción: ")
        if opcion not in opc_correctas:
            print("Por favor, vuelve a intentarlo.")
        else:
            print()       
    return opcion
    
    
def imprimir_jugadores(cursor):
    """Imprimir jugadores existentes en la base de datos

       Parámetros de entrada: cursor de la base de datos
       Parámetros de salida: no hay
    """
    print("IMPRIMIR JUGADORES")
    cursor.execute('select * from JUGADORES')
    reg = cursor.fetchall()
    if not reg:
        print("No existen jugadores.")
    else:
        for jugador in reg:
            print(f'Nombre: {jugador[0]} - Vida: {jugador[1]}')


def existe_jugador(cursor, jugador):
    """Comprueba si existe un jugador en la tabla JUGADORES.

       Parámetros de entrada: cursor de la bd y nombre del jugador
       Parámetros de salida: devuelve True si existe y False en otro caso
    """
    cursor.execute('select nombre from JUGADORES '
                   'where nombre = ?', [jugador,])
    reg = cursor.fetchone()
    if reg is None:
        return False
    else:
        return True



def lee_vida():
    """Pide el valor "vida" por pantalla.

       Parámetros de entrada: no hay
       Parámetros de salida: número entero vida
    """
    correcto = False
    while True:
        try:
            vida = int(input("Dame vida (número positivo): "))
            if vida > 0:
                return vida
            else:
                print("Por favor, ingresa un valor positivo.")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

def existe_credencial(cursor, usuario, contras):
    """Comprueba si existe una credencial en la tabla CREDENCIALES.

       Parámetros de entrada: cursor de la bd, usuario y contraseña.
       Parámetros de salida: devuelve True si existe y False si no.
    """
    cursor.execute('SELECT usuario '
            'FROM CREDENCIALES '
            'WHERE usuario = ? '
            'AND contrasenya = ?', (usuario, contras))

    reg = cursor.fetchone()

    if reg is None:
        print(f'[{usuario}/{contras}] no es una credencial valida')
        return False
    else:
        return True


    
def validar_credencial(cursor):
    """Comprueba si existe el par jugador-contrasenya.

       Parámetros de entrada: cursor de la bd
       Parámetros de salida: no hay
    """
    print("VALIDAR CREDENCIAL")
    nombre = input("Dame jugador: ")
    passwd = input("Dame contrasenya: ")
    if existe_credencial(cursor, nombre, passwd):
        print(f'[{nombre}/{passwd}] si es una credencial valida')
    
def cambiar_credencial(conexion, cursor):
    """Modifica la contraseña de un jugador

       Parámetros de entrada: conexión y cursor de la base de datos
       Parámetros de salida: no hay
    """
    print("CAMBIAR CREDENCIAL")
    nombre = input("Dame jugador: ")
    if not existe_jugador(cursor, nombre):
        print('ERROR: El jugador no existe')
    else:
        pass_vieja = input("Dame contraseña vieja: ")
        if existe_credencial(cursor, nombre, pass_vieja):
            pass_nueva = input("Dame contraseña nueva: ")
            cursor.execute("update CREDENCIALES "
                           "set contrasenya = ? "
                           "where usuario = ?", [pass_nueva, nombre])
            conexion.commit()
            print(f'La contraseña del jugador <{nombre}> se ha modificado correctamente')

def insertar_jugador(conexion, cursor):
    """Inserta un nuevo jugador en la base de datos

       Parámetros de entrada: conexión y cursor de la base de datos
       Parámetros de salida: no hay
    """
    print("INSERTAR JUGADOR")
    nombre = input('Dame nombre: ')
    if not existe_jugador(cursor, nombre):
        vida = lee_vida()
        passwd = input('Dame contraseña: ')

        cursor.execute('insert into JUGADORES '
                       'values (?,?)', [nombre, vida])
        cursor.execute('insert into CREDENCIALES '
                       'values (?,?)', [nombre, passwd])
        conexion.commit()
        print(f'El jugador <{nombre}> se ha insertado correctamente')
    else:
        print('ERROR: El jugador ya existe')
        
       
def borrar_jugador(conexion, cursor):
    """Borra el jugador y sus credenciales de la base de datos

       Parámetros de entrada: conexión y cursor de la base de datos
       Parámetros de salida: no hay
    """
    print("BORRAR JUGADOR")
    nombre = input('Dame el nombre del jugador: ')
    if existe_jugador(cursor, nombre):
        cursor.execute('delete from JUGADORES '
                       'where nombre = ?', [nombre,])
        cursor.execute('delete from CREDENCIALES '
                       'where usuario = ?', [nombre,])
        conexion.commit()
        print(f'Se ha eliminado el jugador <{nombre}> correctamente')
    else:
        print('ERROR: El jugador no existe')


# PROGRAMA PRINCIPAL -------------------------------------------
conexion = sqlite3.connect('bd/ejer_obligatorio.db') #Creamos la conexión a la base de datos
cursor = conexion.cursor() #Creamos el cursor

opcion = valida_opcion()
while opcion != '0':
    if opcion == '1': #Imprimir jugadores
        imprimir_jugadores(cursor)
    elif opcion == '2': #Validar credencial
        validar_credencial(cursor)            
    elif opcion == '3': #Cambiar credencial
        cambiar_credencial(conexion, cursor)
    elif opcion == '4': #Insertar nuevo jugador
        insertar_jugador(conexion, cursor)    
    elif opcion == '5': #Borrar jugador
        borrar_jugador(conexion, cursor)
    opcion = valida_opcion()
conexion.close()