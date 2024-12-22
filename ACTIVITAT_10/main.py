from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from conn.conn import get_db_connection
from db import word_theme
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/penjat/tematica/opcions", response_model=List[dict])
async def retorn_tematica():
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Error en la conexión con la base de datos")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT DISTINCT theme FROM paraules;")
        tematiques = cursor.fetchall()

        return word_theme.tematiques_schema(tematiques)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener las temáticas: {e}")
    finally:
        cursor.close()
        conn.close()

@app.get("/penjat/tematica/{paraula}", response_model=List[dict])
async def retorn_paraula(paraula: str):
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Error en la conexión con la base de datos")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT word FROM paraules WHERE theme = %s;", (paraula,))
        words = cursor.fetchall()

        if words:
            random_word = random.choice(words)[0]
            return [word_theme.paraula_random_schema(random_word)]
        else:
            raise HTTPException(status_code=404, detail="No se encontraron palabras para esta temática")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener la palabra: {e}")
    finally:
        cursor.close()
        conn.close()