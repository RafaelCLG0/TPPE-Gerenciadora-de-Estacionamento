"""Testes para o endpoint de repasses e geração de relatório."""

from datetime import date, datetime
from fastapi.testclient import TestClient
from src.main import app
from src.database import SessionLocal
from src.estacionamento.repository import Estacionamento
from src.acesso.repository import Acesso
from src.relatorios.repository import Relatorio

client = TestClient(app)


def test_calculo_e_registro_relatorio():
    """
    Testa o cálculo de repasses e verifica se o relatório foi salvo no banco.
    """
    db = SessionLocal()

    try:
        # Criação de estacionamento
        response_est = client.post("/estacionamentos/", json={
            "nome": "Estacionamento Teste",
            "cnpj": "12345678000199",
            "valorFracao": 5.0,
            "valorHoraCheia": 10.0,
            "valorDiaria": 50.0,
            "valorMensalista": 200.0,
            "valorEvento": 30.0,
            "valorNoturno": 20.0,
            "horarioNoturnoInicio": "20:00",
            "horarioNoturnoFim": "06:00",
            "percentualRepasse": 15.0,
            "capacidade": 50
        })
        estacionamento_id = response_est.json()["id"]

        # Criação de um acesso comum
        client.post("/acessos/", json={
            "placa": "TEST1234",
            "data_entrada": str(date.today()),
            "hora_entrada": "21:00",
            "data_saida": str(date.today()),
            "hora_saida": "23:00",
            "evento": False,
            "mensalista": False,
            "estacionamento_id": estacionamento_id
        })

        # Chamada ao endpoint de repasses
        inicio = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        fim = datetime.now().replace(hour=23, minute=59, second=59, microsecond=0)

        response = client.get("/relatorios/repasses/", params={
            "inicio": inicio.isoformat(),
            "fim": fim.isoformat()
        })

        assert response.status_code == 200
        data = response.json()
        assert len(data) > 0
        assert data[0]["estacionamento"] == "Estacionamento Teste"
        assert data[0]["total_bruto"] > 0
        assert data[0]["total_repasse"] > 0
        assert data[0]["lucro_liquido"] >= 0

        # Confirma se o relatório foi salvo no banco
        relatorio = db.query(Relatorio).filter(
            Relatorio.estacionamento_id == estacionamento_id
        ).first()

        assert relatorio is not None
        assert relatorio.valor_bruto > 0
        assert relatorio.valor_repasse > 0
        assert relatorio.valor_lucro >= 0

    finally:
        # Limpeza dos dados de teste
        db.query(Relatorio).delete()
        db.query(Acesso).delete()
        db.query(Estacionamento).delete()
        db.commit()
        db.close()
