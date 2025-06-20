import pytest
from fastapi.testclient import TestClient
from datetime import datetime, timedelta
from src.main import app

client = TestClient(app)

# Criar um estacionamento para teste
@pytest.fixture(scope="module")
def estacionamento_padrao():
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
        "percentualRepasse": 10.0
    })
    return response.json()

def test_criar_acesso_com_inferencia(estacionamento_padrao):
    entrada = datetime.now().replace(hour=21, minute=0, second=0, microsecond=0)
    saida = entrada + timedelta(hours=2)

    response = client.post("/acessos/", json={
        "placa": "ABC1234",
        "entrada": entrada.isoformat(),
        "saida": saida.isoformat(),
        "estacionamento_id": estacionamento_padrao["id"]
    })

    assert response.status_code == 200
    data = response.json()
    assert data["placa"] == "ABC1234"
    assert data["estacionamento_id"] == estacionamento_padrao["id"]
    assert "tipo_acesso" in data or "noturno" in str(response.content.decode()).lower()
