from sqlalchemy import create_engine, URL
from sqlalchemy.orm import DeclarativeBase

# datos conexión
url_object = URL.create(
    "mysql",
    username="josaca",
    password="!jJ85211",  # plain (unescaped) text
    host="localhost",
    database="da_josaca",
)


# establecer Declarative Base
class Base(DeclarativeBase):
    pass


# conectar
engine = create_engine(url_object, echo=True)
