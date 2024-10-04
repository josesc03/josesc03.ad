######################################
# UNIDAD 2 - Ejercicio 3             #
# Consultar base de datos (ESQUEMA)  #
######################################

import sqlite3
from pprint import pformat
from pydoc import classname
from xml.dom.minidom import TypeInfo


# DEFINICIÓN DE FUNCIONES --------------------------------------
def valida_opcion():
    '''Función que muestra un menú y valida que la opción sea correcta'''    

    opc_correctas = ['1', '2', '3', '4', '0']
    
    #Mostramos el menú y solicitamos la operación al usuario
    opcion = ''
    while opcion not in opc_correctas:
        print()
        print("========================================")            
        print("         CONSULTAR BASE DE DATOS        ")
        print("========================================")
        print(" 1 - Imprimir jugadores")
        print(" 2 - Imprimir herramientas-jugador ")
        print(" 3 - Consultar jugador")
        print(" 4 - Consultar herramienta-jugador")
        print(" 0 - SALIR ")
        print("--------------------------")    
        opcion = input("Dame la opción: ")
        if opcion not in opc_correctas:
            print("Por favor, vuelve a intentarlo.")
        else:
            print()       
    return opcion
    
def imprimir_jugadores(cursor):
    '''Imprimir jugadores existentes en la base de datos
       
       Parámetros de entrada: cursor de la base de datos
       Parámetros de salida: no hay
    '''
    print("IMPRIMIR JUGADORES")
    cursor.execute('select * from JUGADORES')
    reg = cursor.fetchall()
    for row in reg:
        print(f'Nombre:  {row[0]} + Vida:  + {row[1]}')

def imprimir_herramientas_jugador(cursor):
    '''Imprimir las herramientas de un jugador
       
       Parámetros de entrada: cursor de la base de datos
       Parámetros de salida: no hay
    '''    
    print("HERRAMIENTAS JUGADOR")
    jugador = input('Ingrese el jugador: ')
    cursor.execute('select herramienta from LISTA_HERRAMIENTAS '
                   'where jugador = ?', [jugador,])
    reg = cursor.fetchall()
    print(f'Herramientas: ', end="")
    for row in reg:
            print(row[0], end=" - ")


def consultar_jugador(cursor):
    '''Comprueba si existe un jugador en la tabla JUGADORES.
       
       Parámetros de entrada: cursor de la bd 
       Parámetros de salida: no hay
    '''
    print("CONSULTAR JUGADOR")
    jugador = input('Ingrese el nombre del jugador: ')
    cursor.execute('select * from JUGADORES where nombre = ?', [jugador,])
    reg = cursor.fetchone()
    if reg is None:
        print(f'El jugador {jugador} no existe')
    else:
        print(f'El jugador {jugador} existe')
        print(f'Nombre: {reg[0]} - Vida: {reg[1]}')




def consultar_herramienta_jugador(cursor):
    '''Comprueba si existe el par jugador-herramienta.
       
       Parámetros de entrada: cursor de la bd
       Parámetros de salida: no hay
    '''
    print("CONSULTAR HERRAMIENTA-JUGADOR")
    jugador = input('Dame jugador: ')
    herramienta = input('Dame herramienta: ')
    cursor.execute('select herramienta from LISTA_HERRAMIENTAS '
                   'where jugador = ? AND herramienta = ?', [jugador, herramienta])
    reg = cursor.fetchone()
    if reg is None:
        print(f'El jugador <{jugador}> no tiene una herramienta <{herramienta}>')
    else:
        print(f'El jugador <{jugador}> sí tiene una herramienta <{herramienta}>')




# PROGRAMA PRINCIPAL -------------------------------------------
conexion = sqlite3.connect('ejers_voluntarios_ejer3.db')
cursor = conexion.cursor()

opcion = valida_opcion()
while opcion != '0':
    if opcion == '1': #Imprimir jugadores
        imprimir_jugadores(cursor)
    elif opcion == '2': #Imprimir herramientas-jugadores
        imprimir_herramientas_jugador(cursor)
    elif opcion == '3': #Consultar jugador
        consultar_jugador(cursor)
    elif opcion == '4': #Consultar herramienta-jugador
        consultar_herramienta_jugador(cursor)
        
    opcion = valida_opcion()
conexion.close()