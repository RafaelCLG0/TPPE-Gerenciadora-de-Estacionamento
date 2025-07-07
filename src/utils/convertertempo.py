"""Função utilitária para calcular a duração entre dois datetimes em minutos."""

from datetime import datetime

def calcular_duracao_em_minutos(entrada: datetime, saida: datetime) -> int:
    """
    Retorna a duração total em minutos entre entrada e saída.

    Parâmetros:
    - entrada (datetime): Data e hora de entrada
    - saida (datetime): Data e hora de saída

    Retorna:
    - int: Quantidade total de minutos
    """
    delta = saida - entrada
    return int(delta.total_seconds() // 60)
