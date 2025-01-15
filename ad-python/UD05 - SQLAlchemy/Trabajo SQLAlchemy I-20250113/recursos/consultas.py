
from esquema import engine, Base, Articulo, Vendedor, Pedido, LineaPedido, Provee
from sqlalchemy import select, func, literal_column
from sqlalchemy.orm import Session, aliased

# la sesión para ejecutar todo
sess = Session(engine)

# consulta 1: Nombre de artículos y precio de aquellos que valgan más de 100 euros. 
# El listado debe mostrarse de mayor a menor precio.
stmt = (
    # esto lo hacéis vosotr@s
)

result = sess.execute(stmt)
for row in result:
    print(row)

# consulta 2: Listado de vendedores (nombre) ordenado por el número de pedidos (también se muestra) 
# que han hecho. La ordenación es de mayor a menor.
stmt = (
    # esto lo hacéis vosotr@s
)

result = sess.execute(stmt)
for row in result:
    print(row)


# consulta 3: nombre y cantidad vendida del artículo que más se ha vendido en unidades
# subquery en la que obtenemos para cada artículo la suma de cantidad_pedida
subq = (
    # esto lo hacéis vosotr@s
).cte()
linea_pedido_subq = aliased(LineaPedido, subq)

print(subq)

stmt = (
    # esto lo hacéis vosotr@s
)

result = sess.execute(stmt).first()
for row in result:
    print(row)

# consulta 4: línea de pedido más cara de todas (cantidad_pedida * precio_venta). 
# Debe mostrarse nlinea, npedido y el total de la línea.

stmt = (
    # esto lo hacéis vosotr@s
)

result = sess.execute(stmt).first()
for row in result:
    print(row)

# consulta 5: Realiza una consulta que sirva para rellenar la tabla inventario. Es decir, que 
# obtenga para cada artículo (código) en la fecha a actual la cantidad que hay en stock.

stmt = (
    # esto lo hacéis vosotr@s
)

result = sess.execute(stmt)
for row in result:
    print(row)

sess.close()


