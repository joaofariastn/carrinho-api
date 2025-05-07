from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_adicionar_item():
    response = client.post("/items", json={"id": 1, "nome": "Hamburguer", "preco": 10.0, "quantidade": 2})
    assert response.status_code == 200
    assert response.json()["nome"] == "Hamburguer"

def test_listar_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
