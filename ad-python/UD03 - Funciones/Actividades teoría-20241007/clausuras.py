
# definir funciones dentro de funciones: encapsulamiento de funciones
def telefono_con_prefijo(prefijo_pais):
    def f_telefono(numero_tlf):
        return f'+{prefijo_pais} {numero_tlf}'
    return f_telefono

def beneficios(gastos:list, ingresos:list, tramos_impuestos):
    def obtener_impuesto(ingreso):
        impuesto_actual = tramos_impuestos[0][1]
        for hasta_valor, impuesto in tramos_impuestos:
            if hasta_valor > ingreso:
                break
            else:
                impuesto_actual = impuesto
        return impuesto_actual
    def calculo_neto(ingreso_bruto):
        impuesto = obtener_impuesto(ingreso_bruto)
        return ingreso_bruto - (ingreso_bruto * impuesto)
    gastos_totales = sum(gastos)
    ingresos_netos = sum(map(calculo_neto, ingresos))
    return ingresos_netos - gastos_totales

gastos = [22, 314, 32, 52]
ingresos = [45, 623, 12, 90]
tramos_impuestos = [
    (20, 0.06),
    (50, 0.08),
    (200,0.1),
    (500,0.2),
    (float('Inf'), 0.21)
]
balance_final = beneficios(gastos, ingresos, tramos_impuestos)
print(balance_final)

tlf_españa = telefono_con_prefijo(36)
tlf_aleman = telefono_con_prefijo(96)
tlf_andorra = telefono_con_prefijo(376)
print(tlf_españa(649594927))
print(tlf_aleman(649594927))
print(tlf_andorra(649564627))
