
# función parcial que genera funciones dinámicas que multiplican 
# el argumento final por el argumento que se usa al inicializar
# la función inicial
def f_principal(n):
    '''retorna una función anónima con el parámetro n fijado,
    x se rellena en la llamada a la función
    '''
    return lambda x : x * n

multi_9 = f_principal(9) # n queda instanciado a 9
print(multi_9(10)) # x toma el valor de 10
print(multi_9(80)) # x toma el valor de 80

multi_5 = f_principal(5) # n queda instanciada a 5
print(multi_5(10)) # x toma el valor de 10
print(multi_5(80)) # x toma el valor de 80

