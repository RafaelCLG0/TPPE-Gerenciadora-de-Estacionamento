from src.models.estacionamento import Estacionamento
from src.models.acesso import Acesso

def test_registrar_acesso():
    est = Estacionamento()
    acesso = Acesso(placa="XYZ1234", hora_entrada=8, hora_saida=10)
    est.acessos = []
    est.registrar_acesso(acesso)
    assert len(est.acessos) == 1
    assert est.acessos[0].placa == "XYZ1234"
