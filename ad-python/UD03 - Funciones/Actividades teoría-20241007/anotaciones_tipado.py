

def division(num, deno=1):
    return num / deno

print(division(45, 3)) # 15.0
print(division(45)) # 45.0
print(division(deno=3, num=45)) # argumentos pasados no posicionalmente 
                                # usando los nombres de los parámetros 15.0

def permu( num: int, veces:float) -> float:
    return num * veces

print(permu(7, 2.0)) # 14.0
print(permu("7", 2.0)) # TypeError

def suma_pos(a, b, /):
    return a + b
print(suma_pos(1, 2)) # 3
print(suma_pos(a=1, b=2)) # TypeError

def func(x: int, y:str, z:dict)->bool:
    pass

def foo(elem: float=43.7)->float:
    pass

print(func.__annotations__)

print(foo.__annotations__)

from typing import Counter, Dict, List, Tuple

def bar2(elem1: Counter[str], elem2: Dict[int, float])->List[Tuple[str]]:
    pass