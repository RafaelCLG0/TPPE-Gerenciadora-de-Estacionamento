from fastapi.testclient import TestClient
from src.main import app
from src.core.security import cliente_required
from datetime import datetime

def fake_cliente_required():
    return {"id": 1, "nome": "Usuário Teste"}

app.dependency_overrides[cliente_required] = fake_cliente_required

client = TestClient(app)

def test_aplicar_desconto_seguro():
    estacionamento_payload = {
        "tipo_estacionamento": "Convênio",
        "descricao_hora": 10,
        "taxa_diaria": 100,
        "taxa_evento": 150,
        "contratante": 20,
        "taxa_noturno": 80,
        "taxa_mensal": 300,
        "valor_hora": 20,
        "hora_inicial": 7,
        "hora_final": 19,
        "capacidade": 150
    }
    est_resp = client.post("/estacionamentos/", json=estacionamento_payload)
    assert est_resp.status_code == 200, est_resp.text  # <- garante que não houve erro
    estacionamento_id = est_resp.json()["id"]

    acesso_payload = {
        "placa": "SEG1234",
        "hora_entrada": 9,
        "hora_saida": 11,
        "data_entrada": datetime.now().isoformat(),
        "data_saida": datetime.now().isoformat(),
        "evento": False,
        "mensalista": False,
        "estacionamento_id": estacionamento_id
    }
    acesso_resp = client.post("/acessos/", json=acesso_payload)
    assert acesso_resp.status_code == 200, acesso_resp.text
    acesso_id = acesso_resp.json()["id"]

    desconto = 10
    response = client.post(f"/seguradora/aplicar-desconto/{acesso_id}?desconto={desconto}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert "valor_final" in data
    assert data["desconto_aplicado"] == f"{desconto:.2f}%"
