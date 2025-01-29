from datetime import datetime

from fastapi import FastAPI, HTTPException
from typing import List
from db.text import read as tread
from db.fails import read as fread, add, restart
from db.abc import read as abcread
from db.usertable import  read as utread, edit as utedit
import logging

logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.DEBUG)


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
    return abcread(type_id)

@app.get("/usertable/{user_id}/read", response_model=List[dict])
async def show_user_table(user_id: str):
    return utread(user_id)

@app.post("/usertable/{user_id}/edit/{punts_actuals}{total_partides}{win_partides}{record_time}{record_punts}", response_model=List[dict])
async def edit_user_table(user_id: str, punts_actuals: int, total_partides: int, win_partides: int, record_time: datetime, record_punts: int):
    return utedit(user_id)