

import hashlib
import json

def extraer_identificadores(cadena_original, sep=' '):
    return cadena_original.split(sep)

def aplicar_hash(lst):
    hashes = []
    for cad in lst:
        m = hashlib.sha256()
        m.update(cad.encode('utf-8'))
        hashes.append(m.hexdigest())
    return hashes

def escribir_a_json(data, nombre_fichero='out.json'):
    with open(nombre_fichero, 'w') as f:
        json.dump(data, f)
    return nombre_fichero

cadena_original = 'texto<>a<>guardar'
identificadores = extraer_identificadores(cadena_original, sep='<>')
id_modificados = aplicar_hash(identificadores)
nombre_fichero = escribir_a_json(id_modificados)