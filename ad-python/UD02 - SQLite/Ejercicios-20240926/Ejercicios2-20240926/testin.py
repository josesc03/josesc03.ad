import sqlite3
from datetime import date

def date_to_string(fecha:date, separador='-') -> str:
    return f'{str(fecha.day)}{separador}{str(fecha.month)}{separador}{str(fecha.year)}'

my_conn = sqlite3.connect("test_fechas.db")
my_cur = my_conn.cursor()

sql = '''
create table if not exists amigos (
    id integer primary key autoincrement ,
    nombre text,
    fecha_nac text
    )
'''

my_cur.execute(sql)

def existe_amigo(cur, nombre):
    cur.execute('select nombre from amigos '
                'where nombre = ?', [nombre,])
    if cur.fetchone() is not None:
        return True
    else:
        return False

def importar_amigos(cur):
    nombre = input('Ingrese el nombre del amigo: ')
    if not existe_amigo(cur, nombre):
        dia = int(input('Ingrese día: '))
        mes = int(input('Ingrese mes: '))
        year = int(input('Ingrese año: '))

        fecha = date(year, mes, dia)

        fecha_formateada = date_to_string(fecha)

        my_cur.execute('insert into amigos '
                       'values (null,?,?)', [nombre, fecha_formateada])
    else:
        print('Ese amigo ya existe.')

importar_amigos(my_cur)
my_conn.commit()