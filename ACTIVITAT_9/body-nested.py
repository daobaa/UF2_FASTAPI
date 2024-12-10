from typing import List, Union
from fastapi import FastAPI, Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []

def get_db():
    conn = psycopg2.connect(
        dbname="diego",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
        cursor_factory=RealDictCursor
    )
    try:
        yield conn
    finally:
        conn.close()

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

@app.get("/users/", response_model=List[User])
def read_users(db=Depends(get_db)):
    with db.cursor() as cursor:
        cursor.execute("SELECT id, name, email FROM users")
        users = cursor.fetchall()
    return users