from src.database import SessionLocal
from src.acesso.repository import Acesso
from src.estacionamento.repository import Estacionamento
from fastapi.testclient import TestClient
from datetime import datetime, timedelta
from src.main import app

client = TestClient(app)

def test_integracao_criar_acesso_e_verificar_banco():
    db = SessionLocal()
    try:
        # Criar estacionamento
        estacionamento_resp = client.post("/estacionamentos/", json={
            "nome": "Estac Integrado",
            "cnpj": "11223344556677",
            "valorFracao": 5.0,
            "valorHoraCheia": 10.0,
            "valorDiaria": 40.0,
            "valorMensalista": 250.0,
            "valorEvento": 30.0,
            "valorNoturno": 20.0,
            "horarioNoturnoInicio": "20:00",
            "horarioNoturnoFim": "06:00",
            "percentualRepasse": 8.0,
            "capacidade": 100
        })
        estacionamento_id = estacionamento_resp.json()["id"]

        entrada = datetime.now().replace(hour=21, minute=0, second=0, microsecond=0)
        saida = entrada + timedelta(hours=2)

        client.post("/acessos/", json={
            "placa": "XYZ1234",
            "data_entrada": entrada.date().isoformat(),
            "hora_entrada": entrada.time().isoformat(timespec="minutes"),
            "data_saida": saida.date().isoformat(),
            "hora_saida": saida.time().isoformat(timespec="minutes"),
            "evento": False,
            "mensalista": False,
            "estacionamento_id": estacionamento_id
        })

        acesso = db.query(Acesso).filter(Acesso.placa == "XYZ1234").first()
        assert acesso is not None
        assert acesso.tipo_acesso == "noturno"
    finally:
        db.close()
