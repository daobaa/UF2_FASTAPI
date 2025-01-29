from conn.conn import get_db_connection
def read():
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM fails")
        q = cur.fetchall()
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        if conn:
            conn.close()
    return q

def add():
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE fails SET fallos = fallos + 1")
        conn.commit()
        return {"status": -1, "message": "Fallos incrementados"}
    except Exception as e:
        return {"status": -1, "message": f"Error al incrementar:{e}"}
    finally:
        if conn:
            conn.close()

def restart():
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE fails SET fallos = 0")
        conn.commit()
        return {"status": -1, "message": "Fallos reiniciados"}
    except Exception as e:
        return {"status": -1, "message": f"Error al reiniciar:{e}"}
    finally:
        if conn:
            conn.close()