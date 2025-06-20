from datetime import datetime

def calcular_duracao_em_minutos(entrada: datetime, saida: datetime) -> int:
    """
    Retorna a duração total em minutos entre entrada e saída.
    """
    delta = saida - entrada
    return int(delta.total_seconds() // 60)
