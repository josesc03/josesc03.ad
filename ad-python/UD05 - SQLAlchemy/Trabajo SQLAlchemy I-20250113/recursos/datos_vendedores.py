from conectar import engine
from sqlalchemy import select, Table, MetaData
from sqlalchemy.orm import Session, declarative_base

# interesa desacoplar de crear_tablas una vez creada la BDA con sus tablas
# reflexion de tablas: cargo las tablas desde el SGBD ya que pueden tener datos
Base = declarative_base()
meta = MetaData()

class Vendedor(Base):
    __table__ = Table('vendedores', meta, autoload_with=engine)
    def __repr__(self):
        return f'Vendedor(codigo={self.codigo}, DNI={self.DNI}, nombre={self.nombre}), dcalle={self.dcalle}, dnumero={self.dnumero}, dpiso={self.dpiso}, dlocalidad={self.dlocalidad})'


class Telefono(Base):
    __table__= Table('telefonos', meta, autoload_with=engine) 
    def __repr__(self):
        return f'Telefono(TLF={self.TLF}, codigo_vendedor={self.codigo_vendedor})'


sess = Session(engine)

pepe = Vendedor(DNI='11111111A', nombre='Pepe')
pepa = Vendedor(DNI='22222222B', nombre='Pepa')
pepito = Vendedor(DNI='33333333C', nombre='Pepito')

sess.add(pepe)
sess.add(pepa)
sess.add(pepito)

sess.commit() # me aseguro de insertar primero el lado 1

tlf_pepe_1 = Telefono(TLF='111111111', codigo_vendedor=1)
tlf_pepe_2 = Telefono(TLF='121212121', codigo_vendedor=1)
tlf_pepa_1 = Telefono(TLF='222222222', codigo_vendedor=2)
tlf_pepa_2 = Telefono(TLF='232323232', codigo_vendedor=2)
tlf_pepito_1 = Telefono(TLF='333333333', codigo_vendedor=3)
tlf_pepito_2 = Telefono(TLF='343434343', codigo_vendedor=3)

sess.add(tlf_pepe_1)
sess.add(tlf_pepe_2)
sess.add(tlf_pepa_1)
sess.add(tlf_pepa_2)
sess.add(tlf_pepito_1)
sess.add(tlf_pepito_2)

sess.commit()

# veamos que ha sucedido
result = sess.execute(select(Vendedor))
for row in result:
    print(row)

# veamos que ha sucedido
result = sess.execute(select(Telefono))
for row in result:
    print(row)

sess.close()