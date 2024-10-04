import sqlite3

my_conn = sqlite3.connect("../Actividades teoría-20240924/test.db")
my_cur = my_conn.cursor()

sentencia_sql = ("create table if not exists AFILIACIONES ("
                 "id integer primary key autoincrement,"
                 "persona text,"
                 "fecha_nac date"
                 ")")

my_cur.execute(sentencia_sql)

my_cur.execute("select * from LENGUA_MATERNA")
rows = my_cur.fetchall()
for row in rows:
    print(row)

my_cur.execute('insert into AFILIACIONES '
               'values (null, "1", "15/01/2020")')

my_conn.commit()
my_conn.close()
