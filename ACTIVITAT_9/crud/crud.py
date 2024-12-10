
from typing import List
from psycopg2.extras import RealDictCursor

def get_users(db):
    with db.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("SELECT id, name, email FROM users")
        return cursor.fetchall()
