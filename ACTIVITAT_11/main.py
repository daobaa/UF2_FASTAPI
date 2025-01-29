from fastapi import FastAPI, HTTPException
from typing import List

from conn.conn import get_db_connection
from db.text import read
from db.fails import read, add, restart
from db.abc import read

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/comencar")
async def comencar_partida():
    result = read()
    return {"data": result}

@app.get("/fails")
async def fails():
    f = read()
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
async def lletres(type: int):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT letter FROM abc WHERE type = %s;", (type,))
        q = cur.fetchall()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
    finally:
        if conn:
            conn.close()
    return q