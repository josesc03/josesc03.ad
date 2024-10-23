# sin walrus
n = range(5)
len_n = len(n)
if len_n > 2:
    print(f'{len_n} es mayor que 2')

# sin walrus
print([chr(x) for x in range(0x1100) if chr(x).isnumeric()])

# sin walrus
bruto = 2351
gastos = 456
neto = bruto - gastos
if neto > 0:
    print(f'Neto positivo {neto}')
else:
    print(f'Neto negativo {neto}')

# con walrus
n = range(5)
if (len_n := len(n)) > 2:
    print(f'{len_n} es mayor que 2')

# con walrus
print([c for x in range(0x1100) if (c := chr(x)).isnumeric()])

# con walrus
bruto = 2351
gastos = 456
if (neto := bruto - gastos) > 0:
    print(f'Neto positivo {neto}')
else:
    print(f'Neto negativo {neto}')