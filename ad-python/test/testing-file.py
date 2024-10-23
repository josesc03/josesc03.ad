from re import match

rueda_cifrado = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

contenido_fichero_descifrado = "ANNODENIEVESANNODEBIENES"

contenido_fichero_cifrado = ""
clave = 10

for caracter in contenido_fichero_cifrado:
    if caracter in "¿?¡! 1234567890":  # Si es un espacio, puedes decidir cómo manejarlo
        contenido_fichero_cifrado += caracter
    else:
        index = rueda_cifrado.index(caracter)
        index = index + clave
        if index > 25:
            index -= 26
        elif index < 0:
            index += 26

        contenido_fichero_descifrado += rueda_cifrado[index]

print(contenido_fichero_cifrado)