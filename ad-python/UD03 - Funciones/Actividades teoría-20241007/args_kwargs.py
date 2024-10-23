
def mi_funcion(*args, **kwargs):
    print(f'args: {args}, kwargs: {kwargs}')

mi_funcion() # args: (), kwargs: {}
mi_funcion(42) # args: (42,), kwargs: {}
mi_funcion(vehículo='Coche') # args: (42,), kwargs: {}
mi_funcion(345, 'Juan', modo='Vuelo', flag='Activado')
# args: (345, 'Juan'), kwargs: {'modo': 'Vuelo', 'flag': 'Activado'}

# función general que suministra los parámetros como argumentos 
# de las funciones internas
def calculo_general(**kwargs):
    ret_s = suma(**kwargs)
    ret_d = division(**kwargs)
    return ret_s * ret_d

# define por nombre cada parámetro que se debe usar
# los parámetros que no aparecen están en **kwargs
def suma(op1, op2, **kwargs):
    return op1 + op2

def division(num, deno, **kwargs):
    return num / deno

res = calculo_general(op1=5, op2=9, num=8, deno=2)
print(res) # 56.0

def calculo_general2(*args):
    ret_s = suma2(*args)
    ret_d = division2(*args)
    return ret_s * ret_d

def suma2(op1, op2, *args):
    return op1 + op2

# al acceder posicionalmente se añaden los dos primeros parámetros
# aunque no se utilicen
def division2(a1, a2, num, deno):
    return num /deno
res = calculo_general2(5, 9, 8, 2)
print(res) # 56.0
