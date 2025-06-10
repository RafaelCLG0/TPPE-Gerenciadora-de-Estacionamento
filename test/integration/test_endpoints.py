from fastapi.testclient import TestClient
from src.main import app
from datetime import datetime

client = TestClient(app)

def test_criar_e_listar_estacionamento():
    payload = {
        "tipo_estacionamento": "Rotativo",
        "descricao_hora": 5.0,
        "taxa_diaria": 20,
        "taxa_evento": 50,
        "contratante": 10.0,
        "taxa_noturno": 15.0,
        "taxa_mensal": 200.0,
        "valor_hora": 8.0,
        "hora_inicial": 8,
        "hora_final": 18,
        "capacidade": 100
    }
    r = client.post("/estacionamentos/", json=payload)
    assert r.status_code == 200
    assert r.json()["tipo_estacionamento"] == "Rotativo"

    r = client.get("/estacionamentos/")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_criar_e_listar_acesso():
    est = client.get("/estacionamentos/").json()[0]
    payload = {
        "placa": "ABC1234",
        "hora_entrada": 9,
        "hora_saida": 11,
        "data_entrada": datetime.now().isoformat(),
        "data_saida": datetime.now().isoformat(),
        "evento": False,
        "mensalista": False,
        "estacionamento_id": est["id"]
    }
    r = client.post("/acessos/", json=payload)
    assert r.status_code == 200
    assert r.json()["placa"] == "ABC1234"

    r = client.get("/acessos/")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
