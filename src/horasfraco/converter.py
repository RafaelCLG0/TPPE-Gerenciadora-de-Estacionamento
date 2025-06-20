def calcular_fracoes(duracao_em_minutos: int, minutos_por_fracao: int = 15) -> int:
    """
    Retorna o número de frações baseado na duração e tempo por fração.
    """
    if duracao_em_minutos <= 0:
        return 0
    return (duracao_em_minutos + minutos_por_fracao - 1) // minutos_por_fracao
