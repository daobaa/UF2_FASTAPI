from datetime import datetime

from fastapi import HTTPException
from conn.conn import get_db_connection
from schem.utable_sch import utables_schema


def read(user_id: str):
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute('SELECT punts_actuals, total_partides, win_partides, record_time, record_punts FROM usertable WHERE "user" = %s', (user_id,))
        rows = cur.fetchall()
        result = utables_schema(rows)

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        cur.close()
        conn.close()

def edit(user_id: str, punts_actuals: int, total_partides: int, win_partides: int, record_time: datetime, record_punts: int):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "UPDATE usertable SET punts_actuals = %s, total_partides = %s, win_partides = %s, record_time = %s, record_punts = %s "
            "WHERE user_id = %s", (punts_actuals, total_partides, win_partides, record_time, record_punts, user_id))
        rows = cur.fetchall()

        result = utables_schema(rows)

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        cur.close()
        conn.close()