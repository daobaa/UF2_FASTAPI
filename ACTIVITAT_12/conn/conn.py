import psycopg2

def get_db_connection():
    try:
        connection = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        return connection
    except Exception as e:
        print(f"Error en la conexión a la base de datos: {e}")
        return None