from fastapi import HTTPException
from conn.conn import get_db_connection
from schem.abc_sch import abcs_schema


def read(type_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        if type_id == 2:
            cur.execute("SELECT letter FROM abc;")
        else:
            cur.execute("SELECT letter FROM abc WHERE type = %s;", (type_id,))
        rows = cur.fetchall()

        result = abcs_schema(rows)

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        cur.close()
        conn.close()