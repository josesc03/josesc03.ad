

a = 'Hola'; b = ' Mundo'
def suma(elem1, elem2):
    elem1 += elem2
    return elem1

c = suma(a, b) # al ser elementos no mutables a no se modifica
print(c) # Hola Mundo
print(a) # Hola

a = [1, 2, 3]; b = [4, 5]
c = suma(a, b) # al ser elementos mutables a se modifica
print(c, id(c)) # [1, 2, 3, 4, 5] misma referencia que a
print(a, id(a)) # [1, 2, 3, 4, 5] misma referencia que c

def añadir_valor(elem, lst=[]):
    lst.append(elem)
    return lst

print(añadir_valor(1)) # [1]
print(añadir_valor(2)) # [1, 2]
print(añadir_valor(3)) # [1, 2, 3]

def añadir_valor_seguro(elem, lst=None):
    if lst is None:
        lst = []
    lst.append(elem)
    return lst

print(añadir_valor_seguro(1)) # [1]
print(añadir_valor_seguro(2)) # [2]
print(añadir_valor_seguro(3)) # [3]