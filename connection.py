# import config

import psycopg2
from config import DB_CONFIG

def connect_to_database():
    if not DB_CONFIG["password"]:
        raise ValueError("Password is required")
    try:
        connection = psycopg2.connect(
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            database=DB_CONFIG["database"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"]
        )
        print("✓ Conexión a la base de datos exitosa")
        print(f"  - Host: {DB_CONFIG['host']}")
        print(f"  - Puerto: {DB_CONFIG['port']}")
        print(f"  - Base de datos: {DB_CONFIG['database']}")
        print(f"  - Usuario: {DB_CONFIG['user']}")
        return connection
    except psycopg2.Error as e:
        print(f"✗ Error conectando a la base de datos: {e}")
        return None

def create_table():
    conn = connect_to_database()
    if conn is None:
        print("✗ No se pudo crear la tabla: conexión fallida")
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")
        conn.commit()
        print("✓ Tabla 'users' creada exitosamente")
        print("  - Columnas: id (SERIAL PRIMARY KEY), name (VARCHAR(255)), email (VARCHAR(255))")
        cursor.close()
        conn.close()
        print("✓ Conexión cerrada")
        return True
    except psycopg2.Error as e:
        print(f"✗ Error creando la tabla: {e}")
        if conn:
            conn.close()
        return False