# funciones de orden superior (reciben otras funciones)
# tienen una función interna que satisface una necesidad específica
# y manejan parámetros arbitrarios que se pasan a la función final (args y kwargs)

import time
import string
import functools

def temporiza(func):
    def func_interna(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        tiempo = time.time() - inicio
        print(f'Función {func.__name__} tardó {tiempo}s usando {args} y {kwargs}')
        return resultado
    return func_interna

def convierte_formato(cad):
    lista_elems = list(cad)
    lista_final = []
    for c in lista_elems:
        elem = c.lower() if c.lower() > 'p' else c.upper()
        lista_final.append(elem)
    return ''.join(lista_final)

@temporiza
def suma_elems(elems): #automáticamente decorada
    acc = 0
    for x in elems:
        acc += x
    return acc

@temporiza
@functools.lru_cache(maxsize = 128)
def fibo_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibo_recursivo(n - 1) + fibo_recursivo(n - 2)
    
tempo_formato = temporiza(convierte_formato) #1
print(tempo_formato(string.ascii_letters)) #2
print(tempo_formato("En un lugar de la Mancha")) #2

print(suma_elems(range(1000)))

print(fibo_recursivo(10))
print(fibo_recursivo(10))