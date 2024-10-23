import sys

def contar_rec(elem, acumulador=0):
    if elem == 0:
        return acumulador
    else:
        acumulador += elem
    return contar_rec(elem - 1, acumulador)

print(contar_rec(4))
print(contar_rec(40))

# EJEMPLO1: función que acepte 2 parámetros  como argumentos, pero en caso 
# de no estar inicializados, se definen internamente y se llama
# de nuevo a la función con los nuevos valores.
def simple_func(elem1, elem2=None):
    if elem2 is None:
        return simple_func(elem1, elem2=3) #llamada recursiva
    return elem1 * elem2

print(simple_func(3)) # 9
print(simple_func(3, 4)) # 12

# EJEMPLO2: función que simplifica una estructura compuesta de
# listas anidadas de N niveles. La función debe devolver una 
# versión aplanada de la original, es decir, una lista simple.
def aplanador(llst):
    lista_plana = []
    for elem in llst:
        if isinstance(elem, list):
            lista_plana.extend(aplanador(elem))
        else:
            lista_plana.append(elem)
    return lista_plana

print(aplanador([1, 2, 3, [4, 5, 6], [7, [8, [9]]]]))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

import sys

# EJEMPLO3: función que devuelve el valor de la posición n
# de la secuencia de Fibonacci. Cada elemento se calcula con 
# la suma de los dos elementos anteriores; el primer y segundo
# elemento son los valores 0 y 1 respectivamente.
def fibo(n):
    if n <= 1:
        return n # caso base
    else:
        return fibo(n-1) + fibo(n-2) # llamadas recursivas
    
print([fibo(x) for x in range(26)])
# [0, 1, 1, 2, 3, 5, 8, 13, 21, ... , 28657, 46368, 75025]

print('límite recursión: ', sys.getrecursionlimit())
# límite recursión:  1000




