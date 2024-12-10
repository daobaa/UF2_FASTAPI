from typing import List, Union
from fastapi import FastAPI, Depends
from db_connect.conn import get_db
from schemas.schema import User
from crud.crud import get_users

app = FastAPI()

@app.get("/users/", response_model=List[User])
def read_users(db=Depends(get_db)):
    users = get_users(db)
    return users