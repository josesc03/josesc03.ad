vuelos = [{'origen':'Valencia', 'destino':'Menorca', 'día':'15-08', 'clase':'turista'},
          {'origen':'Valencia', 'destino':'Tenerife', 'día':'20-08', 'clase':'turista'},
          {'origen':'París', 'destino':'Valencia', 'día':'15-08', 'clase':'primera'},
          {'origen':'Atenas', 'destino':'Valencia', 'día':'20-08', 'clase':'primera'} ]

def valida_opcion():

    opciones_validas = ['1', '2', '3', '4', '5', '0']
    opcion = ''
    while (opcion not in opciones_validas):
        print()
        print("=========================")            
        print("     LISTA DE VUELOS     ")
        print("=========================")
        print(" 1 - Imprimir datos vuelos")
        print(" 2 - Buscar por origen ")
        print(" 3 - Imprimir un vuelo")        
        print(" 4 - Cambiar fecha de vuelo ")        
        print(" 0 - SALIR ")
        print("-----------------------------")    
        opcion = input("Dame la opción: ")
        if (opcion not in opciones_validas):
            print("Por favor, vuelve a intentarlo.")
        else:
            print()
    return opcion


def imprimir(lista):
    print("IMPRIMIR VUELOS:")
    c = 0
    for index in lista:
        c += 1
        print(f"\n======== Vuelo {c} ========")
        for clave, valor in index.items():
            clave = clave.capitalize()
            print(f"{clave}: {valor}")
        print("=========================")

def buscar_origen(lista):
    print("BUSCAR ORIGEN:")
    c = 0
    origen = input('Ingrese el origen del vuelo: ')
    for index in lista:
        if index.get('origen') == origen:
            c += 1
            print(f"\n======== Vuelo {c} ========")
            for clave, valor in index.items():
                clave = clave.capitalize()
                print(f"{clave}: {valor}")
            print("=========================")
    if c==0:
        print('No existe ningun vuelo con ese origen.')


def imprimir_vuelo(lista):
    print("IMPRIMIR VUELO:")
    c = 0
    origen = input('Ingrese el origen del vuelo: ')
    destino = input('Ingrese el destino del vuelo: ')
    for index in lista:
        if index.get('origen') == origen.capitalize() and index.get('destino') == destino.capitalize():
            c += 1
            print(f"\n======== Vuelo {c} ========")
            for clave, valor in index.items():
                clave = clave.capitalize()
                print(f"{clave}: {valor}")
            print("=========================")
    if c==0:
        print('No existe ningun vuelo con ese origen y destino.')


def cambiar_fecha(lista):
    print("CAMBIAR FECHA DE VUELO:")
    exists = False
    c = -1
    origen = input('Ingrese el origen del vuelo: ')
    destino = input('Ingrese el destino del vuelo: ')
    for index in lista:
        c += 1
        if index.get('origen') == origen.capitalize() and index.get('destino') == destino.capitalize():
            exists = True
            nueva_fecha = input('Ingrese la nueva fecha del vuelo: ')
            nuevo_vuelo = lista
            nuevo_vuelo[c]['día'] = nueva_fecha
            return nuevo_vuelo
    if exists==False:
        print('No existe ningun vuelo con ese origen y destino.')
        return lista
        

opcion = valida_opcion()
while opcion != '0':          
    if opcion == '1':
        imprimir(vuelos)
    elif opcion == '2': 
        buscar_origen(vuelos)
    elif opcion == '3': 
        imprimir_vuelo(vuelos)
    elif opcion == '4': 
        vuelos = cambiar_fecha(vuelos)
    opcion = valida_opcion()
    
print("Hasta pronto")
