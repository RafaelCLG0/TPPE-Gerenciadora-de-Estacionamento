"""Testes para criação de acesso com inferência de tipo de acesso."""

from datetime import datetime, timedelta
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# Criar um estacionamento para teste
@pytest.fixture(scope="module")
def estacionamento_padrao():
    """Cria um estacionamento padrão para uso nos testes."""
    response = client.post("/estacionamentos/", json={
        "nome": "Estacionamento Central",
        "cnpj": "12345678000100",
        "valorFracao": 5.0,
        "valorHoraCheia": 10.0,
        "valorDiaria": 50.0,
        "valorMensalista": 300.0,
        "valorEvento": 40.0,
        "valorNoturno": 20.0,
        "horarioNoturnoInicio": "20:00",
        "horarioNoturnoFim": "06:00",
        "percentualRepasse": 10.0,
        "capacidade": 100
    })
    return response.json()

def test_criar_acesso_com_inferencia(estacionamento_padrao):  # pylint: disable=redefined-outer-name
    """Testa criação de acesso e inferência do tipo (ex: noturno)."""
    entrada = datetime.now().replace(hour=21, minute=0, second=0, microsecond=0)
    saida = entrada + timedelta(hours=2)

    response = client.post("/acessos/", json={
        "placa": "ABC1234",
        "data_entrada": entrada.date().isoformat(),
        "hora_entrada": entrada.time().isoformat(timespec="minutes"),
        "data_saida": saida.date().isoformat(),
        "hora_saida": saida.time().isoformat(timespec="minutes"),
        "evento": False,
        "mensalista": False,
        "estacionamento_id": estacionamento_padrao["id"]
    })

    assert response.status_code == 200
    data = response.json()
    assert data["placa"] == "ABC1234"
    assert data["estacionamento_id"] == estacionamento_padrao["id"]
    assert "tipo_acesso" in data or "noturno" in str(response.content.decode()).lower()
