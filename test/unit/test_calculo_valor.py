from src.services.calculo_valor import calcular_valor

def test_calcular_valor():
    est = {
        "taxa_mensal": 100,
        "taxa_evento": 70,
        "taxa_noturno": 40,
        "taxa_diaria": 50,
        "descricao_hora": 10,
        "valor_hora": 15
    }
    assert calcular_valor("mensalista", est) == 100
    assert calcular_valor("evento", est) == 70
    assert calcular_valor("noturno", est) == 40
    assert calcular_valor("diaria", est) == 50
    assert calcular_valor("fracao", est) == 10
    assert calcular_valor("hora", est) == 15
    assert calcular_valor("invalido", est) == 0
