

# Partiendo de una cadena de caracteres, se pretende separar la cadena mediante un separador
# y aplicar una función basada en el algoritmo de cifrado md5 a cada elemento para obtener 
# su forma hexadecimal. Una vez obtenida su forma, se ha de guardar en un fichero de texto plano.
import hashlib

def extraer_identificadores(cadena_original, sep=' '):
    return cadena_original.split(sep)

def aplicar_hash(lst):
    md5s = []
    for cad in lst:
        m = hashlib.md5(cad.encode('utf-8'))
        md5s.append(m.hexdigest())
    return md5s

def escribir_a_fichero(data, nombre_fichero='out.txt'):
    with open(nombre_fichero, 'w') as f:
        for d in data:
            f.write(d + '\n')
    return nombre_fichero

cadena_original = 'texto<>a<>guardar'
identificadores = extraer_identificadores(cadena_original, sep='<>')
id_modificados = aplicar_hash(identificadores)
nombre_fichero = escribir_a_fichero(id_modificados)