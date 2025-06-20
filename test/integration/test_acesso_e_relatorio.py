import pytest
from test.utils import get_token, client, garantir_admin

@pytest.mark.skip(reason="Ignorado temporariamente para debug ou ajustes no schema.")
def test_cliente_cria_acesso_com_sucesso():
    garantir_admin()
    admin_token = get_token("admin@test.com", "admin123")
    headers_admin = {"Authorization": f"Bearer {admin_token}"}

    cliente_payload = {
        "nome": "Cliente de Acesso",
        "email": "clienteacesso@teste.com",
        "senha": "cliente123",
        "perfil": "cliente"
    }
    client.post("/usuarios/", json=cliente_payload, headers=headers_admin)

    estacionamento_payload = {
        "tipo_estacionamento": "rotativo",
        "descricao_hora": 10,
        "taxa_diaria": 25,
        "taxa_evento": 20,
        "contratante": 5.0,
        "taxa_noturno": 15.0,
        "taxa_mensal": 300.0,
        "valor_hora": 10.0,
        "hora_inicial": 8,
        "hora_final": 18,
        "capacidade": 100
    }
    est_resp = client.post("/estacionamentos/", json=estacionamento_payload, headers=headers_admin)
    assert est_resp.status_code == 200
    estacionamento_id = est_resp.json()["id"]

    cliente_token = get_token("clienteacesso@teste.com", "cliente123")
    headers_cliente = {"Authorization": f"Bearer {cliente_token}"}

    acesso_payload = {
        "placa": "ABC1234",
        "hora_entrada": 8,
        "hora_saida": 10,
        "data_entrada": "2025-06-11T08:00:00",
        "data_saida": "2025-06-11T10:00:00",
        "evento": False,
        "mensalista": False,
        "estacionamento_id": estacionamento_id
    }

    acesso_resp = client.post("/acessos/", json=acesso_payload, headers=headers_cliente)
    assert acesso_resp.status_code == 200
    assert acesso_resp.json()["placa"] == "ABC1234"
