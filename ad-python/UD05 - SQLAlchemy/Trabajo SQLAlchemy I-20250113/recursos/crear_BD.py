from sqlalchemy_utils import database_exists, create_database, drop_database

from conectar import engine


def crear_bd(depuracion=True):
    '''AQUÍ EN MODO DEPURACIÓN SE BORRA TODO Y SE COMIENZA DE NUEVO'''

    if depuracion:
        # comprobar si existe BDA
        if database_exists(engine.url):
            drop_database(engine.url)

        # comprobar si existe BDA
        if not database_exists(engine.url):
            create_database(engine.url)

    else:
        # comprobar si existe BDA
        if database_exists(engine.url):
            pass

        # comprobar si existe BDA
        if not database_exists(engine.url):
            create_database(engine.url)
