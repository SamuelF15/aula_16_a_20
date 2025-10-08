from typing import Union

from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    nome: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hellow": "World"}

@app.get("/Samuel")
def read_root():
    return {"Família": "Figueiredo"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id * 2, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return{"item_name":item.name, "item_id": item_id}

# response = request.get("http://127.0.0.1:8000")
