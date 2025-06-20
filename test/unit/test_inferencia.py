import pytest
from src.services.inferencia import inferir_tipo_acesso

@pytest.mark.parametrize("entrada,saida,evento,mensalista,esperado", [
    (22, 2, False, False, "noturno"),
    (9, 9, False, False, "fracao"),
    (10, 11, False, False, "hora"),
    (10, 24, False, False, "diaria"),
    (8, 18, True, False, "evento"),
    (8, 18, False, True, "mensalista")
])
def test_inferir_tipo_acesso(entrada, saida, evento, mensalista, esperado):
    assert inferir_tipo_acesso(entrada, saida, evento, mensalista) == esperado
