from datetime import time

def esta_em_turno(hora: time, inicio: time, fim: time) -> bool:
    """
    Verifica se uma hora está dentro de um turno (considera virada de dia).
    """
    if inicio <= fim:
        return inicio <= hora <= fim
    return hora >= inicio or hora <= fim
