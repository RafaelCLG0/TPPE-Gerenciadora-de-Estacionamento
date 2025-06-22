"""Função utilitária para verificação de turno."""

from datetime import time

def esta_em_turno(hora: time, inicio: time, fim: time) -> bool:
    """
    Verifica se uma hora está dentro de um turno, considerando a possibilidade
    de o intervalo cruzar a meia-noite.

    Args:
        hora (time): Hora a ser verificada.
        inicio (time): Início do turno.
        fim (time): Fim do turno.

    Returns:
        bool: True se estiver no turno, False caso contrário.
    """
    if inicio <= fim:
        return inicio <= hora <= fim
    return hora >= inicio or hora <= fim
