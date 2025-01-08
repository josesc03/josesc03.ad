import mysql.connector
from mysql.connector import connection


def mostrar_tabla(cursor, table_name):
    try:
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        rows = cursor.fetchall()
        if rows:
            print(f"\n{Colores.INFO}Datos de la tabla '{table_name}':{Colores.RESET}")
            for row in rows:
                print(row)

        else:
            print(f"{Colores.INFO}La tabla '{table_name}' está vacía.{Colores.RESET}")
    except Exception as e:
        print(f"{Colores.ERROR}Error al mostrar la tabla '{table_name}': {e}{Colores.RESET}")


# Colores para mensajes
class Colores:
    EXITO = "\033[92m"  # Verde
    ERROR = "\033[91m"  # Rojo
    INFO = "\033[94m"  # Azul
    RESET = "\033[0m"  # Reset color


# Conexión a la base de datos
cnx = connection.MySQLConnection(user='josaca', password='85211', host='localhost')
print(f"{Colores.EXITO}Conectado{Colores.RESET}\n")

# Crear cursor
cursor = cnx.cursor()

# Seleccionar la base de datos
use_query = "USE DA_josaca"
cursor.execute(use_query)

# Diccionario con las definiciones de las tablas
TABLES = {}

TABLES['borrar_tablas'] = """
    DROP TABLE IF EXISTS notas;
    DROP TABLE IF EXISTS alumnos;
    DROP TABLE IF EXISTS modulos;
"""

TABLES['alumnos'] = """
    CREATE TABLE alumnos (
        expediente CHAR(8) PRIMARY KEY,
        nombre VARCHAR(30) NOT NULL,
        apellidos VARCHAR(50) NOT NULL
    );
"""

TABLES['modulos'] = """
    CREATE TABLE modulos (
        codigo VARCHAR(5) PRIMARY KEY,
        nombre VARCHAR(30) NOT NULL
    );
"""

TABLES['notas'] = """
    CREATE TABLE notas (
        expediente CHAR(8),
        codigo VARCHAR(5),
        nota INTEGER UNSIGNED,
        PRIMARY KEY (expediente, codigo),
        CONSTRAINT fk_expediente
            FOREIGN KEY (expediente)
            REFERENCES alumnos(expediente)
            ON DELETE CASCADE ON UPDATE CASCADE,
        CONSTRAINT fk_codigo
            FOREIGN KEY (codigo)
            REFERENCES modulos(codigo)
            ON DELETE CASCADE ON UPDATE CASCADE
    );
"""

# Ejecutar las definiciones de las tablas
for table_name, table_query in TABLES.items():
    try:
        if table_name == 'borrar_tablas':
            print(f"{Colores.INFO}Eliminando tablas...{Colores.RESET}")
        else:
            print(f"{Colores.INFO}Creando la tabla {table_name}...{Colores.RESET}")
        for statement in table_query.split(";"):
            if statement.strip():  # Evitar sentencias vacías
                cursor.execute(statement)
        if table_name == 'borrar_tablas':
            print(f"{Colores.EXITO}Tablas eliminadas con éxito.{Colores.RESET}")
        else:
            print(f"{Colores.EXITO}Tabla {table_name} creada con éxito.{Colores.RESET}")
    except Exception as e:
        print(f"{Colores.ERROR}Error al crear la tabla {table_name}: {e}{Colores.RESET}")

cnx.commit()

TRIGGERS = {}

TRIGGERS['auditoria_notas'] = """
    DROP TABLE IF EXISTS auditoria_notas;
    CREATE TABLE auditoria_notas (
        id SERIAL PRIMARY KEY,
        expediente_old CHAR(8),
        codigo_old VARCHAR(5),
        nota_old INTEGER UNSIGNED,
        expediente_new CHAR(8),
        codigo_new VARCHAR(5),
        nota_new INTEGER UNSIGNED,
        usuario VARCHAR(50) NOT NULL,
        cuando DATETIME NOT NULL,
        operacion ENUM('insert', 'update', 'delete') NOT NULL
    );
"""

TRIGGERS['auditoria_notas_insert'] = """
    DROP TRIGGER IF EXISTS auditoria_notas_insert;
    CREATE TRIGGER auditoria_notas_insert AFTER INSERT ON notas
    FOR EACH ROW
    INSERT INTO auditoria_notas
    VALUES (
        NULL, NULL, NULL, NULL,
        NEW.expediente, NEW.codigo, NEW.nota,
        USER(), NOW(), 'insert'
    );
"""

TRIGGERS['auditoria_notas_update'] = """
    DROP TRIGGER IF EXISTS auditoria_notas_update;
    CREATE TRIGGER auditoria_notas_update AFTER UPDATE ON notas
    FOR EACH ROW
    INSERT INTO auditoria_notas
    VALUES (
        NULL, OLD.expediente, OLD.codigo, OLD.nota,
        NEW.expediente, NEW.codigo, NEW.nota,
        USER(), NOW(), 'update'
    );
"""

TRIGGERS['auditoria_notas_delete'] = """
    DROP TRIGGER IF EXISTS auditoria_notas_delete;
    CREATE TRIGGER auditoria_notas_delete AFTER DELETE ON notas
    FOR EACH ROW
    INSERT INTO auditoria_notas
    VALUES (
        NULL, OLD.expediente, OLD.codigo, OLD.nota,
        NULL, NULL, NULL,
        USER(), NOW(), 'delete'
    );
"""

# Ejecutar las definiciones de los triggers
for trigger_name, trigger_query in TRIGGERS.items():
    try:
        print(f"{Colores.INFO}Creando el trigger {trigger_name}...{Colores.RESET}")
        for statement in trigger_query.split(";"):
            if statement.strip():  # Evitar sentencias vacías
                cursor.execute(statement)
        print(f"{Colores.EXITO}Trigger {trigger_name} creado con éxito.{Colores.RESET}")
    except Exception as e:
        print(f"{Colores.ERROR}Error al crear el trigger {trigger_name}: {e}{Colores.RESET}")

cnx.commit()

INSERT = {}

INSERT['alumnos'] = """
    INSERT INTO alumnos VALUES
        ('11111111', 'Alexia', 'Núñez Pérez'),
        ('22222222', 'Rosa', 'Fernández Oliva'),
        ('33333333', 'Peter', 'Linuesa Jiménez'),
        ('44444444', 'Juan Carlos', 'Wesnoth The Second'),
        ('55555555', 'Federico', 'Muñoz Ferrer');
"""

INSERT['modulos'] = """
    INSERT INTO modulos VALUES
        ('QP', 'Quirománcia Práctica'),
        ('MR', 'Mortum Redivivus'),
        ('RF', 'Refactorización Zómbica'),
        ('ARF', 'Ampliación de RF'),
        ('OP', 'Orquestación de Plagas');
"""

INSERT['notas'] = """
    INSERT INTO notas VALUES
        ('11111111', 'QP', 5),
        ('11111111', 'RF', 6),
        ('11111111', 'ARF', 9),
        ('11111111', 'OP', 7),
        ('22222222', 'QP', NULL),
        ('22222222', 'MR', 5),
        ('22222222', 'RF', 5),
        ('22222222', 'ARF', 6),
        ('22222222', 'OP', NULL),
        ('33333333', 'QP', 9),
        ('33333333', 'MR', 5),
        ('33333333', 'RF', 6),
        ('33333333', 'ARF', 4),
        ('33333333', 'OP', 6),
        ('44444444', 'QP', 5),
        ('44444444', 'MR', 5),
        ('44444444', 'RF', 5),
        ('44444444', 'ARF', 6),
        ('44444444', 'OP', 5),
        ('55555555', 'QP', 5),
        ('55555555', 'MR', 7),
        ('55555555', 'RF', 6),
        ('55555555', 'ARF', 7),
        ('55555555', 'OP', 5);
"""

# Ejecutar las definiciones de los inserts
for insert_name, insert_query in INSERT.items():
    try:
        print(f"{Colores.INFO}Creando el insert {insert_name}...{Colores.RESET}")
        # for statement in insert_query.split(";"):
        #     if statement.strip():  # Evitar sentencias vacías
        cursor.execute(insert_query)
        print(f"{Colores.EXITO}Insert {insert_name} creado con éxito.{Colores.RESET}")
    except Exception as e:
        print(f"{Colores.ERROR}Error al crear el insert {insert_name}: {e}{Colores.RESET}")

cnx.commit()

try:
    cursor.execute("DROP FUNCTION IF EXISTS expediente_correcto;")
    cursor.execute("""
        CREATE FUNCTION expediente_correcto(exp VARCHAR(8)) RETURNS TINYINT(1)
            DETERMINISTIC
            NO SQL
        BEGIN
            RETURN exp REGEXP '^[0-9]{8}$';
        END;
    """)
    print(f"{Colores.EXITO}Función 'expediente_correcto' creada con éxito.{Colores.RESET}")
except mysql.connector.Error as e:
    print(f"{Colores.ERROR}Error al crear la función 'expediente_correcto': {e}{Colores.RESET}")

cnx.commit()

# Pruebas con expedientes
print(f"\n{Colores.INFO}Mostrando funcionalidad de la función 'expediente_correcto': {Colores.RESET}")
expedientes_prueba = ['11111111', 'abcdefgh', '12345678']
query = "SELECT expediente_correcto(%s)"

for exp in expedientes_prueba:
    try:
        cursor.execute(query, (exp,))
        resultado = cursor.fetchone()
        print(f"Expediente '{exp}': {'Válido' if resultado[0] == 1 else 'No válido'}")
    except mysql.connector.Error as e:
        print(f"Error al validar el expediente '{exp}': {e}")

# Mostrar tablas para verificar inserciones
for table_name in TABLES.keys():
    if table_name != 'borrar_tablas':
        mostrar_tabla(cursor, table_name)


def pasan_a_segundo(cursor):
    alumnos = {}
    try:
        query = (f"SELECT codigo FROM modulos")
        cursor.execute(query)
        codigos = cursor.fetchall()
        for i in range(len(codigos)):
            codigos[i] = codigos[i][0]

        query = (f"SELECT expediente, nombre FROM alumnos")
        cursor.execute(query)
        expedientes = cursor.fetchall()
        if expedientes:
            for expediente in expedientes:
                query = (f"SELECT nota, codigo FROM notas "
                         f"WHERE expediente = {expediente[0]}")
                alumnos[expediente[0]] = True
                cursor.execute(query)
                notas = cursor.fetchall()

                # quitar si se quiere
                print(f"\n{Colores.INFO}Notas del alumno con expediente {expediente[0]}:{Colores.RESET}\n"
                      f"{notas}")

                modulos_presentes = {modulo for _, modulo in notas}

                if not all(modulo in modulos_presentes for modulo in codigos):
                    alumnos[expediente[0]] = False
                    continue

                sumaNotas = 0
                for nota, _ in notas:
                    if nota is None:
                        alumnos[expediente[0]] = False
                        continue
                    if nota < 5:  # revisar
                        alumnos[expediente[0]] = False
                        continue
                    else:
                        sumaNotas += nota

                if alumnos[expediente[0]] is False:
                    continue

                if sumaNotas / len(notas) < 6:
                    alumnos[expediente[0]] = False
                    continue

        else:
            print(f"{Colores.INFO}La tabla '{table_name}' está vacía.{Colores.RESET}")

        personas_aprobadas = [expediente for expediente, aprobado in alumnos.items() if aprobado]
        personas_aprobadas_str = f"({', '.join(personas_aprobadas)})"
        print(personas_aprobadas_str)

        query = (f"SELECT nombre, apellidos from alumnos "
                 f"WHERE expediente in {personas_aprobadas_str}")

        cursor.execute(query)
        aprobados = cursor.fetchall()
        print(f"\n{Colores.INFO}Personas que pasan a segundo: {Colores.RESET}")
        for aprobado in aprobados:
            print(aprobado[0], aprobado[1])

        print(
            f"\n{Colores.INFO}Porcentaje de aprobados: {(len(personas_aprobadas) / len(alumnos) * 100)}% {Colores.RESET}")

    except Exception as e:
        print(f"{Colores.ERROR}Error al mostrar la tabla '{table_name}': {e}{Colores.RESET}.")


print(f"\n{Colores.INFO}Ejecutando método \"pasan_a_segundo\":{Colores.RESET}")
pasan_a_segundo(cursor)
print(f"\n{Colores.EXITO}Método ejecutado con éxito.")

cnx.commit()
cursor.close()
cnx.close()
print(f"{Colores.EXITO}\nDesconectado{Colores.RESET}")
