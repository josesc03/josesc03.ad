
import sqlite3

my_conn = sqlite3.connect(":memory:") # BDA temporal

# un cursor es un objeto que permite ejecutar intrucciones SQL en una BDA
my_cur = my_conn.cursor() # creamos cursor

# instrucciones de uso del cursor
# DDL: la sentencia va sin ; al final 
# tb. podemos pasar una variable str que contenga SQL
my_cur.execute("create table TEST(id INTEGER, field1 TEXT, Primary Key(id))")
my_conn.commit() # hace permanentes los cambios en la BDA (transacción)

my_conn.close()
