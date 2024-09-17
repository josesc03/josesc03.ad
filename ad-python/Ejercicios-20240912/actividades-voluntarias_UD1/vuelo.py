vuelo = {
    "origen": "valencia",
    "destino": "menorca",
    "dia": "15-08",
    "clase": "turista"
}

while True:
    print('''=========================
   GESTION DE UN VUELO   
=========================
 1 - Imprimir datos vuelo
 2 - Imprimir claves
 3 - Añadir <pasajeros>
 4 - Imprimir un valor
 5 - Borrar clave
 0 - SALIR
-------------------------''')
    while True:
        try:
            opcion = int(input("Dame la opcion: "))
        except:
            print("Tienes que dar un numero entero")
        else:
            if opcion not in (1,2,3,4,5,0):
                print("Opcion fuera de rango")
            else:
                break

    if opcion == 1:
        print(vuelo)
    elif opcion == 2:
        print(list(vuelo.keys()))
    elif opcion == 3:
        numeroPasajeros = int(input("Numero de pasajeros: "))
        vuelo["pasajeros"] = numeroPasajeros
    elif opcion == 4:
        opcionClave = input("Indica la clave que quieres buscar: ")
        if opcionClave in vuelo.keys():
            print(f"{opcionClave}: {vuelo.get(opcionClave)}")
        else:
            print("Esa clave no existe.")
    elif opcion == 5:
        opcionClave = input("Indica la clave que quieres buscar: ")
        if opcionClave in vuelo.keys():
            vuelo.pop(opcionClave)
        else:
            print("Esa clave no existe.")
    elif opcion == 0:
        break
