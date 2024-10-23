
def range_personal(inicio, fin, paso=1):
    final = inicio
    while final < fin:
        yield final
        final += paso

def fibo_generador():
    previo = 0
    actual = 1
    yield 0
    while True:
        yield actual
        previo, actual = actual, actual + previo

print(list(range_personal(0, 20, 3)))
fibo_g = fibo_generador()
print([next (fibo_g) for _ in range(15)])

f = range_personal(0, 10, 6)
print(next(f))
print(next(f))
print(next(f)) #exhausto excepción StopIteration