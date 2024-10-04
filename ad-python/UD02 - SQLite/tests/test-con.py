import sqlite3

my_conn = sqlite3.connect("../Actividades teoría-20240924/test.db")

my_cur = my_conn.cursor()

sentencia_sql = '''create table if not exists LENGUA_MATERNA(
abreviatura TEXT,
nombre TEXT,
descripcion TEXT,
PRIMARY KEY(abreviatura)
)
'''

my_cur.execute(sentencia_sql)
my_conn.commit()
my_conn.close()