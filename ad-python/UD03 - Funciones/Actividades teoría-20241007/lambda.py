
f_x3 = lambda x: x*3
print(f_x3(10))

lst = ['a1', 'a12', 'a100', 'a5']
print(sorted(lst)) #ordenado por caracter
print(sorted(lst, key=lambda x: int(x[1:]))) #ordenación numérica correcta

lst = [1, 425, 3421, 34, 2]
lst.sort(key=lambda x: (x < 400, x)) #ordenaciones de varios parámetros usando tuplas
print(lst)

print(lst)
print(min(lst))
print(min(lst, key=lambda x: x < 50))

print(lst)
print(max(lst, key=lambda x: x**2 > 500))
print(max(lst, key=lambda x: x * 2 < 50 and not x % 2))

print(list(map(lambda x: x + 34, range(5))))
print([x + 34 for x in range(5)]) # por comprensión
print(list(map(lambda x: x.title(), ['juan', 'pedro', 'ana'])))
print([x.title() for x in ['juan', 'pedro', 'ana']]) # por comprensión

print(list(filter(lambda x: not x % 5, range(100))))
print([x for x in range(100) if not x % 5]) # por comprensión
print(list(filter(lambda x: 'e' in x.lower(), ['Perico', 'Papá', 'Mamá'])))