

def foo():
    pass

def menor_valor(iter):
    return min(iter)

def iniciales(cadena, sep = ' '):
    "Devuelve las iniciales de cada palabra en la cadena separadas por sep"
    return ''.join(x[0].upper() for x in cadena.split(sep))

print('foo(): ', foo())
foo()

print('menor_valor([1, 2, 3, 4]): ', menor_valor([1, 2, 3, 4]))

print("iniciales('Natxo Febrer Senar'): ", iniciales('Natxo Febrer Senar'))


