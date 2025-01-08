import os
import platform
import pydoc
import random
import time

limpiar_consola = 'cls' if platform.system() == 'Windows' else 'clear'

# Constantes
rueda_cifrado = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def castigar_usuario(a):
    """
    Impone un castigo sombrío al usuario, congelando el flujo del programa por su temeraria negligencia
    al ingresar datos incorrectos. Este método se asegura de que sienta las consecuencias de sus errores
    a través de una pausa temporal en la ejecución.
    """
    time.sleep(a)

def limpiar_texto(texto):
    """
    Realiza una limpieza en el texto para prepararlo para el cifrado:
    elimina acentos, convierte caracteres especiales y lo transforma a mayúsculas.

    :param texto: str Texto a procesar.
    :return: str Texto limpio y en mayúsculas, listo para ser cifrado.
    """
    return (texto
            .replace('ñ', 'nn')
            .replace('á', 'a')
            .replace('é', 'e')
            .replace('í', 'i')
            .replace('ó', 'o')
            .replace('ö', 'o')
            .replace('ú', 'u')
            .replace('ü', 'u')
            .replace('\n', ' ')
            .replace('\r', ' ')
            .upper())

def proceso_finalizado():
    """
    Muestra un mensaje visual que indica que el proceso ha finalizado correctamente.
    """
    print("\n========================================")
    print("         ✔ Proceso Finalizado ✔")
    print("========================================\n")

def procesar(dicc):
    """Lee el fichero del diccionario y lo procesa: sin tildes ni diéresis, mayúsculas
    y Ñ -> NN. Retorna un set sin \n o \r\n al final de cada elemento.

    :param dicc: str Nombre del fichero que contiene palabras en castellano
    :returns: list Lista de palabras procesada. Lista vacia en caso de error
    """

    print("\n" + "=" * 30)
    print(" " * 7 + "🟢 PROCESANDO 🟢")
    print("=" * 30 + "\n")

    try:
        d = open(dicc, 'r', encoding='latin-1')

        todo = d.read()
        todo = limpiar_texto(todo)
        d.close()

        miset = set(todo.split(' '))
        return miset
    except FileNotFoundError:
        print(f'Error: El archivo "{dicc}" no se encontró.')
        castigar_usuario(1)
        return set()
    except PermissionError:
        print(f'Error: Permiso denegado para el archivo "{dicc}".')
        castigar_usuario(1)
        return set()
    except Exception as e:
        print(f"Error inesperado: {e}")
        castigar_usuario(1)
        return set()

def max_palabra(set_palabras):
    """
    Retorna el tamaño máximo de palabra en el set de palabras en castellano

    :param set_palabras: set(str) set de palabras en castellano
    :returns:
    int Tamaño máximo encontrado
    """

    mayor = 0
    for palabra in set_palabras:
        if len(palabra) > mayor:
            mayor = len(palabra)

    return mayor

def num_coincidencias(set_palabras, texto_candidato, min_sub=1, max_sub=None):
    """
    Compara todas las posibles subcadenas de texto_candidato entre los tamaños
    min_sub y max_sub contra el set de palabras

    :param set_palabras: list todas las palabras del castellano
    :param texto_candidato: str Texto en el que se buscan coincidencias dentro de la lista
    :param min_sub: int Tamaño mínimo de subcadena a buscar
    :param max_sub: int Tamaño máximo de subcadena a buscar

    :returns:
    int Número de coincidencias en el diccionario
    """

    coincidencias = 0
    longitud_texto = len(texto_candidato) + 1
    texto_candidato = texto_candidato.upper()

    if max_sub is None:
        max_sub = max_palabra(set_palabras)

    for i in range(longitud_texto):
        for j in range(min_sub, max_sub + 1):
            if i + j >= longitud_texto:
                break
            palabra_texto = texto_candidato[i:i+j]

            if palabra_texto in set_palabras:

                coincidencias += 1
    return coincidencias

def texto_plano(fichero_texto_plano:str):
    """Pide al ususario que escriba un texto y se guarda en un fichero. Se pide línea a línea
    y ,para acabar, pulsamos INTRO y luego CTRL + D

    :param fichero_texto_plano: str nombre del fichero donde se guarda el texto plano
    """

    print("\n" + "-" * 25)
    print(" " * 4 + "📄 TEXTO PLANO 📄")
    print("-" * 25 + "\n")

    try:
        with open(fichero_texto_plano, 'w', encoding='latin-1') as file:
            print("Escribe el texto. Para finalizar, pulsa ENTER sin escribir nada:")

            while True:
                linea = input()
                piezas = linea.split(" ")
                if not linea:
                    break
                file.write(linea + '\n')
        print(f"Texto guardado en {fichero_texto_plano}")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")

def cifrar(fichero_texto_plano, fichero_cifrado_cesar):
    """
    Dado un fichero de texto en plano y una clave aplica el cifrado César según los
    requerimientos: eliminar espacios y signos de puntuación,
    vocal con tildes -> sin tildes, min -> MAY, Ñ -> NN, texto cifrado 5 en 5
    comenzando por la izquierda.
    ASUMO que los números se quedan igual y caracteres tipo: ¡!¿? también
    La clave utilizada será aleatoria de 1 a 25.

    :param fichero_texto_plano: str nombre de fichero con el Texto a cifrar.
    Se procesa para cumplir requisitos
    :param fichero_cifrado_cesar: str nombre de fichero donde se guardan el texto cifrado

    :returns:
    str | None Texto cifrado para la clave aleatoria o None si hubo algún error
    """
    print("\n" + "-" * 30)
    print(" " * 8 + "🔒 CIFRANDO 🔒")
    print("-" * 30 + "\n")

    try:
        with open(fichero_texto_plano, 'r', encoding='latin-1') as f:
            contenido = f.read()
            print("Fichero plano leido correctamente\n")
            contenido = limpiar_texto(contenido)
            contenido = contenido.replace(" ", "")
            print("Antes: "+ contenido)

            contenido_formateado = ""
            contador = 0
            for letras in contenido:
                contenido_formateado+=letras
                contador += 1
                if contador == 5:
                    contenido_formateado += " "
                    contador = 0

        print("Despues: "+ contenido_formateado+"\n")

    except FileNotFoundError:
        print(f"Error: El archivo '{fichero_texto_plano}' no existe.")
        castigar_usuario(1)
    except PermissionError:
        print(f"Error: No tienes permisos para abrir el archivo '{fichero_texto_plano}'.")
        castigar_usuario(1)
    except Exception as e:
        print(f"Error inesperado: {e}")
        castigar_usuario(1)

    try:
        with open(fichero_cifrado_cesar, 'w', encoding="latin-1") as file:
            print("Fichero de cifrado abierto correctamente")
            contenido_fichero_cifrado = ""
            clave = random.randint(1,25)

            for caracter in contenido_formateado:
                if caracter not in rueda_cifrado:
                    contenido_fichero_cifrado += caracter

                else:
                    index = rueda_cifrado.index(caracter)
                    index = index + clave
                    if index > 25:
                        index -= 26
                    elif index < 0:
                        index += 26

                    contenido_fichero_cifrado += rueda_cifrado[index]

            file.write(contenido_fichero_cifrado)
            print(f"\nTexto cifrado guardado en {fichero_cifrado_cesar}")

    except FileNotFoundError:
        print(f"Error: El archivo '{fichero_cifrado_cesar}' no existe.")
        castigar_usuario(1)
    except PermissionError:
        print(f"Error: No tienes permisos para abrir el archivo '{fichero_cifrado_cesar}'")
        castigar_usuario(1)
    except Exception as e:
        print(f"Error inesperado: {e}")
        castigar_usuario(1)

    return None

def descifra(fichero_cifrado_cesar, fichero_texto_plano_candidato, clave):
    """
    Dado un texto cifrado (del fichero_cifrado_cesar) y una clave realiza un
    desplazamiento en sentido contrario a dicha clave. El resultado se guarda en
    fichero_texto_plano_candidato y se pone como sufijo la clave empleada

    :param fichero_cifrado_cesar: str nombre del fichero con el texto a descifrar
    :param fichero_texto_plano_candidato: str nombre del fichero con el texto tras
    aplicar la clave en sentido contrario para descifrar
    :param clave: int clave a aplicar. De 1 a 25

    :returns: str | None texto descifrado o None si hubo algún error
    """

    try:
        with open(fichero_cifrado_cesar, 'r', encoding="latin-1") as file:
            contenido_fichero_cifrado = file.read()
            print("Fichero cifrado leido correctamente")
    except FileNotFoundError:
        print(f"Error: El archivo '{fichero_cifrado_cesar}' no existe.")
        castigar_usuario(1)
    except PermissionError:
        print(f"Error: No tienes permisos para abrir el archivo '{fichero_cifrado_cesar}'.")
        castigar_usuario(1)
    except Exception as e:
        print(f"Error inesperado: {e}")
        castigar_usuario(1)

    try:
        with open(fichero_texto_plano_candidato, 'w', encoding="latin-1") as file:
            descifrado = descifras(contenido_fichero_cifrado, clave)
            file.write(descifrado)
            print("Fichero descifrado escrito correctamente")
            return descifrado
    except FileNotFoundError:
        print(f"Error: El archivo '{fichero_cifrado_cesar}' no existe.")
        castigar_usuario(1)
    except PermissionError:
        print(f"Error: No tienes permisos para abrir el archivo '{fichero_cifrado_cesar}'.")
        castigar_usuario(1)
    except Exception as e:
        print(f"Error inesperado: {e}")
        castigar_usuario(1)

    return None

def descifras(texto_cifrado, clave):
    """
    Dado un texto cifrado realiza un desplazamiento en sentido contrario de la rueda según la clave

    :param texto_cifrado: str Cadena con el texto cifrado
    :param clave: int Valor de la clave (1 a 25)

    :returns:
    str Texto descifrado
    """
    contenido_descifrado = ""
    clave = clave * -1

    for caracter in texto_cifrado:
        if caracter in "¿?¡!,.;: 1234567890":
            contenido_descifrado += caracter
        else:
            index = rueda_cifrado.index(caracter)
            index = index + clave
            if index > 25:
                index -= 26
            elif index < 0:
                index += 26

            contenido_descifrado += rueda_cifrado[index]

    return contenido_descifrado

def descifrar_fuerza_bruta(fichero_cifrado_cesar, fichero_resultados):
    """
    Abre el fichero con el texto cifrado y saca los textos correspondientes
    a intentos de descifrar con las claves de 0 a 26 (en realidad solo hace falta
    de 1 a 25).

    :param fichero_cifrado_cesar: str Fichero con el texto cifrado
    :param fichero_resultados: str se generan 25 ficheros como resultado de aplicar todas las claves.
    La clave aplicada aparece como sufijo en el nombre del fichero

    :returns:
    stdout Todos los textos precedidos de la clave aplicada en cada caso.
    """

    print("\n" + "-" * 30)
    print(" " * 5 + "🔍 DESCIFRAR BRUTA 🔍")
    print("-" * 30 + "\n")

    try:
        with open(fichero_cifrado_cesar, 'r', encoding="latin-1") as file:
            contenido_fichero_cifrado = file.read()
            print("Fichero cifrado leido correctamente")
            file.close()
    except FileNotFoundError:
        print(f"Error: El archivo '{fichero_cifrado_cesar}' no existe.")
        castigar_usuario(1)
    except PermissionError:
        print(f"Error: No tienes permisos para abrir el archivo '{fichero_cifrado_cesar}'.")
        castigar_usuario(1)
    except Exception as e:
        print(f"Error inesperado: {e}")
        castigar_usuario(1)

    try:

        if not os.path.exists("resultado"):
            os.makedirs('resultado')

        descifrado = ""
        archivo = ""

        for i in range(1,26):
            archivo = f"resultado/{fichero_resultados}_clave{i}.txt"
            with open(archivo, 'w', encoding="latin-1") as file:
                descifrado_unilateral = descifras(contenido_fichero_cifrado, i)
                descifrado += descifrado_unilateral + "\n"
                file.write(descifrado_unilateral)
                file.close()
        print(f"\nArchivos guardados en el fichero resultado")
        return descifrado

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no existe.")
        castigar_usuario(1)
    except PermissionError:
        print(f"Error: No tienes permisos para abrir el archivo '{archivo}'.")
        castigar_usuario(1)
    except Exception as e:
        print(f"Error inesperado: {e}")
        castigar_usuario(1)

    return None

def descifrar_fuerza_bruta_dic(fichero_cifrado_cesar, fichero_resultado, diccionario:set , porcentaje=0.25, rapido=False, minPalabra=None, maxPalabra=None):
    """
    Abre el fichero con el texto cifrado y saca los textos correspondientes
    a intentos de descifrar con las claves de 0 a 26 (en realidad solo hace falta
    de 1 a 25). Por cada texto, indica el número de subcadenas que coinciden con
    entradas del diccionario

    :param fichero_cifrado_cesar: str Fichero con el texto cifrado
    :param fichero_resultado: str Fichero con los resultados (texto y coincidencias) de aplicar todas las claves
    :param diccionario: list lista de palabras en castellano
    :param porcentaje: int Aquellas claves que generen un porcentaje (en tanto por 1) de coincidencias cercano a
    la mejor (porcentaje 1) tal que 1 - porcentaje <= coincidencias <= 1 serán consideradas como solución
    alternativa
    :param rapido: boolean Si es False mira todas las posibles subcadenas. Si es True pide la longitud mínima y
    máxima de las cadenas a considerar. De esta forma, si se hace con criterio, se acelera bastante la búsqueda
    en el diccionario
    :param minPalabra: int Tamaño mínimo de palabra a considerar
    :param maxPalabra: int Tamaño máximo de palabra a considerar

    :returns:
    stdout Todos los textos precedidos de la clave aplicada en cada caso. Como
    side-effect crea un fichero con los resultados. Si hay algún tipo de error
    informa de ello
    """

    print("\n" + "-" * 40)
    print(" " * 2 + "🔍 DESCIFRA BRUTA POR DICCIONARIO 🔍")
    print("-" * 40 + "\n")
    time.sleep(2)

    try:
        with open(fichero_cifrado_cesar, 'r', encoding="latin-1") as file:
            contenido_fichero_cifrado = file.read()
            if contenido_fichero_cifrado == "":
                raise Exception("El fichero cifrado esta vacio.")

        if not os.path.exists("resultado"):
            os.makedirs("resultado")

        descifrado_completo = ""

        for clave in range(1, 26):
            descifrado_unilateral = descifras(contenido_fichero_cifrado, clave)
            archivo_salida = f"resultado/{fichero_resultado}_clave{clave}.txt"
            with open(archivo_salida, 'w', encoding="latin-1") as file:
                file.write(descifrado_unilateral)

            texto_sin_espacios = descifrado_unilateral.replace(" ", "")
            if rapido and minPalabra is not None and maxPalabra is not None:
                coincidencias = num_coincidencias(diccionario, texto_sin_espacios, minPalabra, maxPalabra)
            else:
                coincidencias = num_coincidencias(diccionario, texto_sin_espacios, 1)

            if coincidencias / len(descifrado_unilateral) >= (porcentaje):
                descifrado_completo += (
                    f"Clave {clave}: Coincidencias {coincidencias}\n"
                    f"{descifrado_unilateral}\n\n"
                )
        return descifrado_completo
    except FileNotFoundError:
        print(f"Error: El archivo '{fichero_cifrado_cesar}' no existe.")
        castigar_usuario(1)
    except PermissionError:
        print(f"Error: No tienes permisos para abrir el archivo '{fichero_cifrado_cesar}'.")
        castigar_usuario(1)
    except Exception as e:
        print(f"Error inesperado: {e}")
        castigar_usuario(1)

def menu():
    os.system(limpiar_consola)
    print('''
 ██████ ██ ███████ ██████   █████  ██████   ██████       ██████ ███████ ███████  █████  ██████  
██      ██ ██      ██   ██ ██   ██ ██   ██ ██    ██     ██      ██      ██      ██   ██ ██   ██ 
██      ██ █████   ██████  ███████ ██   ██ ██    ██     ██      █████   ███████ ███████ ██████  
██      ██ ██      ██   ██ ██   ██ ██   ██ ██    ██     ██      ██           ██ ██   ██ ██   ██ 
 ██████ ██ ██      ██   ██ ██   ██ ██████   ██████       ██████ ███████ ███████ ██   ██ ██   ██''')
    print('\n*** Hackeando, a lo bruto, a Julio César ***')
    print('1) Crear fichero en texto plano')
    print('2) Cifrar fichero')
    print('3) Fuerza bruta y resolución a "ojo"')
    print('4) Fuerza bruta y resolución por diccionario')
    print('5) Salir')

    opcion = input('Escoge opción: ')
    while opcion not in '12345' or opcion == "":
        opcion = input('Escoge opción (entre 1 y 5): ')
    os.system(limpiar_consola)

    return int(opcion)


def es_flotante_adecuado(porcentaje):
    """
    Comprueba si es un float adecuado: 0.0 <= porcentaje <= 1.0

    :returns:
    bool
    """
    try:
        porcentaje = float(porcentaje)
        if 0.0 <= porcentaje <= 1.0:
            return True
        else:
            return False
    except:
        return False


def es_int_adecuado(numero, minimo, maximo):
    """
    Comprueba si es un int adecuado: minimo <= numero <= maximo

    :returns:
    bool
    """
    try:
        numero = int(numero)
        if minimo <= numero <= maximo:
            return True
        else:
            return False
    except:
        return False


if __name__== "__main__":

    while True:
        opcion = menu()

        if opcion == 1:
            nombre_fichero = input("Introduce el nombre del archivo plano: ").strip()
            if nombre_fichero:
                texto_plano(nombre_fichero + '.txt')
            else:
                print("El nombre del archivo no puede estar vacío.")
                castigar_usuario(1)
            proceso_finalizado()
            time.sleep(1)

        elif opcion == 2:
            nombre_fichero = input("Introduce el nombre del archivo a cifrar: ").strip()
            if nombre_fichero:
                cifrar(nombre_fichero + '.txt', nombre_fichero + '_cifrado.txt')
            else:
                print("El nombre del archivo no puede estar vacío.")
                castigar_usuario(1)
            proceso_finalizado()
            time.sleep(3)

        elif opcion == 3:
            nombre_fichero = input("Introduce el nombre del archivo cifrado: ").strip()
            if nombre_fichero:
                descifrar_fuerza_bruta(nombre_fichero + '_cifrado.txt', nombre_fichero + '_descifrado')
            else:
                print("El nombre del archivo no puede estar vacío.")
                castigar_usuario(1)
            proceso_finalizado()
            time.sleep(2)


        elif opcion == 4:
            nombre_fichero = input("Introduce el nombre del archivo cifrado: ").strip()
            if nombre_fichero:
                # Manejar el porcentaje con un valor predeterminado
                porcentaje_input = input("Introduce el porcentaje de coincidencias para considerar un resultado válido (0.25 por defecto): ").strip()

                if porcentaje_input == "":
                    porcentaje = 0.25  # Valor por defecto
                    print("Se ha utilizado el porcentaje por defecto: 0.25")
                else:
                    try:
                        porcentaje = float(porcentaje_input)
                        if not es_flotante_adecuado(porcentaje):
                            raise ValueError  # Forzar la entrada a seguir pidiendo si no es adecuada
                    except ValueError:
                        print("Por favor, introduce un número válido para el porcentaje.")
                        castigar_usuario(1)
                        continue

                rapido = input("¿Quieres que sea rápido? (F/T): ").strip().upper() == 'T'
                minimo = maximo = None

                if rapido:
                    while True:
                        try:
                            minimo = int(input("Introduce el mínimo: ").strip())
                            maximo = int(input("Introduce el máximo: ").strip())
                            if minimo <= maximo:
                                break
                            else:
                                print("El mínimo no puede ser mayor que el máximo, vuelve a intentarlo.")
                        except ValueError:
                            print("Por favor, introduce un número entero válido.")
                else:
                    rapido = False
                os.system(limpiar_consola)

                resultados = descifrar_fuerza_bruta_dic(
                    nombre_fichero + '_cifrado.txt',
                    nombre_fichero + '_diccionario',
                    procesar("Diccionario.txt"),
                    porcentaje,
                    rapido,
                    minimo,
                    maximo
                )
                if resultados is not None:

                    if platform.system() == "Linux":
                        resultados += "\n\nPulse Q para salir."

                    pydoc.pager(str(resultados))


            else:
                print("El nombre del archivo no puede estar vacío.")
            time.sleep(1)
            if platform.system() == "Windows":
                input("Pulse Enter para continuar")
            proceso_finalizado()
            time.sleep(2)

        elif opcion == 5:
            print("\n========================================")
            print("  👋 ¡Gracias por usar el programa! 👋")
            print("             ¡Hasta pronto!             ")
            print("========================================\n")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")
            castigar_usuario(1)