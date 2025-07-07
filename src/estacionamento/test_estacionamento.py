"""Testes dos endpoints de criação e listagem de Estacionamentos."""

from fastapi.testclient import TestClient

from src.main import app
from src.database import SessionLocal
from src.estacionamento.repository import Estacionamento

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

    limpar_estacionamentos()


def test_listar_estacionamentos():
    """
    Testa a listagem de todos os estacionamentos cadastrados.
    """
    response = client.get("/estacionamentos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    limpar_estacionamentos()


def limpar_estacionamentos():
    """
    Remove estacionamentos criados nos testes.
    """
    db = SessionLocal()
    db.query(Estacionamento).delete()
    db.commit()
    db.close()
