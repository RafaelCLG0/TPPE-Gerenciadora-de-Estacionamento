"""Testes unitários para criação e listagem de usuários via API."""

import os
import sys

from fastapi.testclient import TestClient
from src.main import app

# Permite execução direta dos testes
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

client = TestClient(app)

def test_criar_usuario():
    """Testa a criação de um usuário com perfil ADMIN."""
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
    """Testa a listagem de usuários cadastrados."""
    response = client.get("/usuarios/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
