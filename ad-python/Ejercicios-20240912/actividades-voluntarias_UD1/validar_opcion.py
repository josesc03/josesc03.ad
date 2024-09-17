def valida_opcion():
    '''
    Funcion para validar
    '''

    while True:
        print('''=============================
   GAMIFICACIÓN EN EL AULA
=============================
 1 - Cargar los datos del fichero
 2 - Imprimir datos
 3 - Jugar
 4 - Guardar datos
 5 - Cambiar contraseña
 0 - SALIR
-----------------------------''')
        eleccion = int(input("Dame la opción: "))
        if eleccion > 6 or eleccion < 0:
            print('Por favor. vuelve a intentarlo')
        else:
            print(f'La opción seleccionada es: {eleccion}')
            if eleccion == 0:
                print('Saliendo...')
                break

valida_opcion()