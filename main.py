from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Simple FastAPI App")


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


# In-memory "database"
items: dict[int, Item] = {}
next_id = 1


@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/items")
def list_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.post("/items", status_code=201)
def create_item(item: Item):
    global next_id
    items[next_id] = item
    next_id += 1
    return {"id": next_id - 1, "item": item}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return item


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"deleted": item_id}
