from logging import exception

jugadores = ["jugador1", "jugador2", "jugador3", "jugador4"]


def nuevoJugador():
    nombre = input("¿Quién eres? ")
    print(f"Bienvenid@ jugador {nombre}")
    jugadores.append(nombre)


def seVaJugador():
    print(f"Adios jugador {jugadores[0]}")
    jugadores.pop(0)


while True:
    print('''===========================
JUGADORES ON-LINE     
 1 - Llega un jugador nuevo
 2 - Se va un jugador
 3 - FIN
---------------------------''')
    while True:
        try:
            opcion = int(input("Dame la opcion: "))
        except:
            print("Tienes que dar un numero entero")
        else:
            if opcion not in (1,2,3):
                print("Opcion fuera de rango")
            else:
                break

    if opcion == 1:
        nuevoJugador()
    elif opcion == 2:
        seVaJugador()
    elif opcion == 3:
        break

    print(jugadores)
