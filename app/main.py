from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

carrinho = []

class Item(BaseModel):
    id: int
    nome: str
    preco: float
    quantidade: int

@app.post("/items", response_model=Item)
def adicionar_item(item: Item):
    carrinho.append(item)
    return item

@app.get("/items", response_model=List[Item])
def listar_items():
    return carrinho

@app.put("/items/{item_id}", response_model=Item)
def atualizar_item(item_id: int, item: Item):
    for i, existente in enumerate(carrinho):
        if existente.id == item_id:
            carrinho[i] = item
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")

@app.delete("/items/{item_id}")
def remover_item(item_id: int):
    for i, existente in enumerate(carrinho):
        if existente.id == item_id:
            del carrinho[i]
            return {"message": "Item removido"}
    raise HTTPException(status_code=404, detail="Item não encontrado")
