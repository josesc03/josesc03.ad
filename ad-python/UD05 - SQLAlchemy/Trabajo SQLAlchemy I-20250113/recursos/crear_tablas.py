from datetime import date
from conectar import engine, Base
from crear_BD import crear_bd
from sqlalchemy import String, Date, Numeric, ForeignKey
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship

# creamos en modo depuración
crear_bd()

# creación de tablas
'''
IMPORTANTE: Las políticas de FK se gestionan en el servidor
Es decir, al crear la columna FK se indica la política en la tabla del lado M.
A parte se crean las listas en el lado 1 para que el ORM tenga a mano los datos.
Las relationship son bidireccionales.
''' 

# Vendedor
class Vendedor(Base):
    __tablename__ = 'vendedores'

    codigo: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    DNI: Mapped[str] = mapped_column(String(9), unique=True)
    nombre: Mapped[str] = mapped_column(String(75))
    
    dcalle: Mapped[Optional[str]] = mapped_column(String(50))
    dnumero: Mapped[Optional[str]] = mapped_column(String(5))
    dpiso: Mapped[Optional[str]] = mapped_column(String(5))
    dlocalidad: Mapped[Optional[str]] = mapped_column(String(50))

    # lista de teléfonos del vendedor + borrados/modificaciones en cascada
    telefonos: Mapped[List["Telefono"]] = relationship(
        back_populates="vendedor",
        cascade="all, delete",
        passive_deletes=True,
        passive_updates=True
    )
    # lista de pedidos que ha hecho el vendedor
    pedidos: Mapped[List["Pedido"]] = relationship(
        back_populates="vendedor",
        cascade="all, delete",
        passive_deletes=True,
        passive_updates=True,
    )
    
    def __repr__(self):
        return f'Vendedor(codigo={self.codigo}, DNI={self.DNI}, nombre={self.nombre}), dcalle={self.dcalle}, dnumero={self.dnumero}, dpiso={self.dpiso}, dlocalidad={self.dlocalidad})'

# Telefono
class Telefono(Base):
    __tablename__ = 'telefonos'

    TLF: Mapped[str] = mapped_column(String(9), primary_key=True)
    codigo_vendedor: Mapped[int] = mapped_column(ForeignKey("vendedores.codigo", ondelete="CASCADE", onupdate="CASCADE"))

    # vendedor propietario del teléfono
    vendedor: Mapped["Vendedor"] = relationship(back_populates="telefonos")

    def __repr__(self):
        return f'Telefono(TLF={self.TLF}, codigo_vendedor={self.codigo_vendedor})'
    
# Pedido
class Pedido(Base):
    __tablename__ = 'pedidos'

    npedido: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fecha : Mapped[date] = mapped_column(Date)

    codigo_vendedor: Mapped[int] = mapped_column(ForeignKey("vendedores.codigo", ondelete="RESTRICT", onupdate="CASCADE"))
    # vendedor que ha hecho el pedido
    vendedor: Mapped["Vendedor"] = relationship(back_populates="pedidos")

    '''este código se debe comentar mientras no se tenga la class LineaPedido '''
    # líneas de pedido de ese pedido
    lineas: Mapped[List["LineaPedido"]] = relationship(
        back_populates="pedido",
        cascade="all, delete",
        passive_deletes=True,
        passive_updates=True,
    )

    def __repr__(self):
        return f'Pedido(npedido={self.npedido}, fecha={self.fecha}, codigo_vendedor={self.codigo_vendedor})'


Base.metadata.create_all(engine)

