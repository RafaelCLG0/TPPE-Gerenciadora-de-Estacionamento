"""Testes de integração: criação de usuário e verificação no banco de dados."""

import os
import sys

from fastapi.testclient import TestClient

from src.database import SessionLocal
from src.usuario.repository import Usuario
from src.main import app

# Ajuste do path para execução isolada do teste
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

client = TestClient(app)

def test_integracao_criar_usuario_e_verificar_banco():
    """Cria um usuário via API e verifica se foi persistido corretamente no banco."""
    db = SessionLocal()
    try:
        client.post("/usuarios/", json={
            "nome": "Cliente",
            "email": "cliente@example.com",
            "senha": "1234",
            "perfil": "CLIENTE"
        })

        usuario = db.query(Usuario).filter(Usuario.email == "cliente@example.com").first()
        assert usuario is not None
        assert usuario.nome == "Cliente"
        assert usuario.perfil == "CLIENTE"
    finally:
        db.close()
