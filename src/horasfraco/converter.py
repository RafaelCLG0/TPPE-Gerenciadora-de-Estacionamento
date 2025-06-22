"""Função para calcular o número de frações de tempo com base na duração em minutos."""

def calcular_fracoes(duracao_em_minutos: int, minutos_por_fracao: int = 15) -> int:
    """
    Retorna o número de frações baseado na duração e tempo por fração.

    Parâmetros:
    - duracao_em_minutos (int): Tempo total do acesso em minutos.
    - minutos_por_fracao (int): Quantidade de minutos por fração (default: 15).

    Retorna:
    - int: Quantidade de frações cobradas.
    """
    if duracao_em_minutos <= 0:
        return 0
    return (duracao_em_minutos + minutos_por_fracao - 1) // minutos_por_fracao
