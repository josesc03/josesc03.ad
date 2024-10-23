
v_global = 10
def foo(x):
    return x + v_global # podemos leerla

def foo2(x):
    v_global += 10 # actualización no permitida
    return v_global + x

def foo3(x):
    global v_global # permite leer y actualizar
    v_global += 10
    return v_global + x

def foo_correct():
    ruedas = 4
    def pinchar_rueda(): # permite acceder al contexto superior
        nonlocal ruedas
        ruedas -= 1
    print(f'Número de ruedas: {ruedas}')
    pinchar_rueda()
    print(f'Número de ruedas: {ruedas}')

def pecera():
    pez = 'Dori'
    x = 5
    print(f'Locals: {locals()}')
    print(f'Globals: {globals()}')

pez = 'Nemo'
pecera()

foo_correct()

print(foo(5))
# print(foo2(5))
print(foo3(5))
