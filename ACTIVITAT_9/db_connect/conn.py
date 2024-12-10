import psycopg2
from psycopg2.extras import RealDictCursor

def get_db():
    conn = psycopg2.connect(
        dbname="diego",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
        cursor_factory=RealDictCursor
    )
    try:
        yield conn
    finally:
        conn.close()