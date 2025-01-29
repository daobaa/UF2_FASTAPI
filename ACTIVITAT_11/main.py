from fastapi import FastAPI, HTTPException
from typing import List

from conn.conn import get_db_connection
from db.text import read as tread
from db.fails import read as fread, add, restart
from db.abc import read
from schem.abc_sch import abcs_schema

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/comencar")
async def comencar_partida():
    result = tread()
    return {"data": result}

@app.get("/fails")
async def fails():
    f = fread()
    return {"fallos": f}

@app.post("/fails")
async def fails_add():
    f = add()
    return {"message": f["message"]}

@app.post("/0fails")
async def fails_restart():
    f = restart()
    return {"message": f["message"]}

@app.get("/abc/{type}", response_model=List[dict])
async def lletres(type_id: int):
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
        if cur:
            cur.close()
        if conn:
            conn.close()

@app.get("/usertable/{user}/show", response_model=List[dict])
async def show_user_table(user_id: str):
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute("SELECT punts_actuals, total_partides, win_partides, record_time, record_punts FROM usertable WHERE user = %s", (user_id,))
        result = cur.fetchall()

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()