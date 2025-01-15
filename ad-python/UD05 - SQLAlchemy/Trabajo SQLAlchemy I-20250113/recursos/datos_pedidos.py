from datetime import date

from sqlalchemy import select, Table, MetaData
from sqlalchemy.orm import Session, declarative_base

from conectar import engine

# interesa desacoplar de crear_tablas una vez creada la BDA con sus tablas
# reflexion de tablas: cargo las tablas desde el SGBD ya que pueden tener datos
Base = declarative_base()
meta = MetaData()


class Vendedor(Base):
    __table__ = Table('vendedores', meta, autoload_with=engine)

    def __repr__(self):
        return f'Vendedor(codigo={self.codigo}, DNI={self.DNI}, nombre={self.nombre}), dcalle={self.dcalle}, dnumero={self.dnumero}, dpiso={self.dpiso}, dlocalidad={self.dlocalidad})'


class Telefono(Base):
    __table__ = Table('telefonos', meta, autoload_with=engine)

    def __repr__(self):
        return f'Telefono(TLF={self.TLF}, codigo_vendedor={self.codigo_vendedor})'


class Pedido(Base):
    __table__ = Table('pedidos', meta, autoload_with=engine)

    def __repr__(self):
        return f'Pedido(npedido={self.npedido}, fecha={self.fecha}, codigo_vendedor={self.codigo_vendedor})'


sess = Session(engine)

p11 = Pedido(fecha=date(2025, 1, 7), codigo_vendedor=1)
p12 = Pedido(fecha=date(2025, 1, 8), codigo_vendedor=1)
p13 = Pedido(fecha=date(2025, 1, 9), codigo_vendedor=1)
p21 = Pedido(fecha=date(2025, 1, 6), codigo_vendedor=2)
p22 = Pedido(fecha=date(2025, 1, 7), codigo_vendedor=2)

sess.add(p11)
sess.add(p12)
sess.add(p13)
sess.add(p21)
sess.add(p22)

sess.commit()

# veamos que ha sucedido
result = sess.execute(select(Vendedor))
for row in result:
    print(row)

# veamos que ha sucedido
result = sess.execute(select(Telefono))
for row in result:
    print(row)

# veamos que ha sucedido
result = sess.execute(select(Pedido))
for row in result:
    print(row)

sess.close()
