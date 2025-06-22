"""Testes dos endpoints de criação e listagem de Estacionamentos."""

import os
import sys
from fastapi.testclient import TestClient

from src.main import app

# Adiciona o caminho base ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

client = TestClient(app)

def test_criar_estacionamento():
    """
    Testa a criação de um novo estacionamento com dados válidos.
    """
    response = client.post("/estacionamentos/", json={
        "nome": "Estacionamento Sul",
        "cnpj": "98765432000100",
        "valorFracao": 3.0,
        "valorHoraCheia": 6.0,
        "valorDiaria": 30.0,
        "valorMensalista": 200.0,
        "valorEvento": 25.0,
        "valorNoturno": 15.0,
        "horarioNoturnoInicio": "22:00",
        "horarioNoturnoFim": "05:00",
        "percentualRepasse": 12.0,
        "capacidade": 75
    })
    assert response.status_code == 200
    data = response.json()
    assert data["cnpj"] == "98765432000100"

def test_listar_estacionamentos():
    """
    Testa a listagem de todos os estacionamentos cadastrados.
    """
    response = client.get("/estacionamentos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
