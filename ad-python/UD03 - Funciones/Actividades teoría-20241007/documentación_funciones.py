
def suma_pares(elems):
    """Suma los elementos pares encontrados en elems

    :param elems: lista de números por sumar

    :return integer: número resultante de la suma de los pares
    """
    return sum(x for x in elems if not x % 2)


help(suma_pares)
print(suma_pares.__doc__)