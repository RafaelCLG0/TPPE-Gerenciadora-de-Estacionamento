"""Funções para inferência do tipo de acesso com base nos horários."""

from datetime import datetime

def is_horario_noturno(hora, inicio, fim):
    """
    Verifica se a hora está dentro do intervalo noturno,
    inclusive quando cruza a meia-noite.
    """
    if inicio < fim:
        return inicio <= hora <= fim
    return hora >= inicio or hora <= fim

def inferir_tipo_acesso(
    entrada: datetime,
    saida: datetime,
    horario_noturno_inicio: str,
    horario_noturno_fim: str
) -> str:
    """
    Inferir o tipo de acesso com base na duração e horário do acesso.

    Parâmetros:
    - entrada: datetime de entrada
    - saida: datetime de saída
    - horario_noturno_inicio: string no formato "HH:MM"
    - horario_noturno_fim: string no formato "HH:MM"

    Retorna:
    - str: tipo de acesso ('noturno', 'diaria', 'hora_cheia', 'fracao', 'invalido')
    """
    if saida < entrada:
        return "invalido"

    duracao = saida - entrada
    horas = duracao.total_seconds() / 3600

    noturno_inicio = datetime.strptime(horario_noturno_inicio, "%H:%M").time()
    noturno_fim = datetime.strptime(horario_noturno_fim, "%H:%M").time()

    entrada_em_noturno = is_horario_noturno(entrada.time(), noturno_inicio, noturno_fim)
    saida_em_noturno = is_horario_noturno(saida.time(), noturno_inicio, noturno_fim)

    if entrada_em_noturno and saida_em_noturno:
        return "noturno"
    if horas >= 9:
        return "diaria"
    if horas >= 1:
        return "hora_cheia"
    if horas > 0:
        return "fracao"
    return "invalido"
