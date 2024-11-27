from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class ALUM(BaseModel):
    name: str
    surname: str
    birth_year: int
    list_num: int
    email: str
    phone_num: int | None = None

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hola Mundo"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/alumne")
async def add_alum(alum: ALUM):
    return alum
