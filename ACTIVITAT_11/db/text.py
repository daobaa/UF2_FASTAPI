from conn.conn import get_db_connection
def read():
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM comencar")
        q = cur.fetchall()
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        if conn:
            conn.close()
    return q