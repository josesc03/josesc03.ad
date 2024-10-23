# aquellas que aceptan otras funciones como parámetros

import math

def op(a, b, func):
    return func(a, b)

def raiz_de_par(x):
    if not x % 2:
        return math.sqrt(x)
    return 0

def mul_de_par(x, multi=5):
    if not x % 2:
        return x * multi
    return 0

def aplicar_func(lst, func):
    return [func(x) for x in lst]

r1 = op(45, 75, int.__add__)
r2 = op(45, 75, int.__mul__)
print(r1, r2)

r3 = aplicar_func(range(20), mul_de_par)
print(r3)

r4 = aplicar_func(range(20), raiz_de_par)
print(r4)

mul_de_par_8 = lambda x: mul_de_par(x, multi=8) # función parcial
r5 = aplicar_func(range(20), mul_de_par_8)
print(r5)