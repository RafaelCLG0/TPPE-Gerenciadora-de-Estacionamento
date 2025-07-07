"""Testes unitários para criação e listagem de usuários via API."""

from fastapi.testclient import TestClient
from src.main import app
from src.database import SessionLocal
from src.usuario.repository import Usuario

client = TestClient(app)


def test_criar_usuario():
    """
    Testa a criação de um usuário com perfil ADMIN.
    """
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

    limpar_usuarios()


def test_listar_usuarios():
    """
    Testa a listagem de usuários cadastrados.
    """
    response = client.get("/usuarios/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    limpar_usuarios()


def limpar_usuarios():
    """
    Remove usuários criados nos testes.
    """
    db = SessionLocal()
    db.query(Usuario).delete()
    db.commit()
    db.close()
