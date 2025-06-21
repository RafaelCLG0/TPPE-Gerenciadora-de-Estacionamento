from fastapi.testclient import TestClient
from src.main import app
from datetime import date

client = TestClient(app)

def criar_estacionamento_padrao(cnpj):
    response = client.post("/estacionamentos/", json={
        "nome": "Estac Centro",
        "cnpj": cnpj,
        "valorFracao": 4.0,
        "valorHoraCheia": 8.0,
        "valorDiaria": 35.0,
        "valorMensalista": 200.0,
        "valorEvento": 45.0,
        "valorNoturno": 25.0,
        "horarioNoturnoInicio": "20:00",
        "horarioNoturnoFim": "06:00",
        "percentualRepasse": 10.0,
        "capacidade": 50
    })
    return response.json()["id"]

def test_acesso_evento():
    estacionamento_id = criar_estacionamento_padrao("00011122200091")
    response = client.post("/acessos/", json={
        "placa": "EVENTO123",
        "data_entrada": str(date.today()),
        "hora_entrada": "18:00",
        "data_saida": str(date.today()),
        "hora_saida": "22:00",
        "evento": True,
        "mensalista": False,
        "estacionamento_id": estacionamento_id
    })
    assert response.status_code == 200
    data = response.json()
    assert data["tipo_acesso"] == "evento"
    assert data["valor_pago"] == 45.0

def test_acesso_mensalista():
    estacionamento_id = criar_estacionamento_padrao("00011122200092")
    response = client.post("/acessos/", json={
        "placa": "MENSAL123",
        "data_entrada": str(date.today()),
        "hora_entrada": "10:00",
        "data_saida": str(date.today()),
        "hora_saida": "18:00",
        "evento": False,
        "mensalista": True,
        "estacionamento_id": estacionamento_id
    })
    assert response.status_code == 200
    data = response.json()
    assert data["tipo_acesso"] == "mensalista"
    assert data["valor_pago"] == 200.0
