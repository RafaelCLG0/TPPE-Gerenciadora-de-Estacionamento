from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_criar_usuario():
    response = client.post("/usuarios/", json={
        "nome": "Admin",
        "email": "admin@example.com",
        "senha": "1234",
        "perfil": "ADMIN"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "admin@example.com"
    assert data["perfil"] == "ADMIN"

def test_listar_usuarios():
    response = client.get("/usuarios/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
