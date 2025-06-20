from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_criar_estacionamento():
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
        "percentualRepasse": 12.0
    })
    assert response.status_code == 200
    data = response.json()
    assert data["cnpj"] == "98765432000100"

def test_listar_estacionamentos():
    response = client.get("/estacionamentos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
