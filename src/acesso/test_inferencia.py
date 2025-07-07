"""Teste para a função de inferência do tipo de acesso no sistema de estacionamento."""

from datetime import datetime
import pytest

from src.acesso.inferencia import inferir_tipo_acesso


@pytest.mark.parametrize("entrada_hora, saida_hora, tipo_esperado", [
    ("21:00", "23:00", "noturno"),
    ("08:00", "08:30", "fracao"),
    ("08:00", "09:30", "hora_cheia"),
    ("08:00", "18:00", "diaria"),
])
def test_inferir_tipo_acesso(entrada_hora, saida_hora, tipo_esperado):
    """
    Testa a função inferir_tipo_acesso com diferentes faixas de horário,
    simulando situações reais de entrada e saída.
    """
    hoje = datetime.today().replace(minute=0, second=0, microsecond=0)
    entrada = hoje.replace(hour=int(entrada_hora[:2]), minute=int(entrada_hora[3:]))
    saida = hoje.replace(hour=int(saida_hora[:2]), minute=int(saida_hora[3:]))
    tipo = inferir_tipo_acesso(entrada, saida, "20:00", "06:00")
    assert tipo == tipo_esperado
