input = int(input('Dame un número entero del 1 al 10: '))
print(f'TABLA DE MULTIPLICAR DEL Nº {input}:')
for i in range(10):
    print(i+1," * ", input,' = ', input*(i+1))