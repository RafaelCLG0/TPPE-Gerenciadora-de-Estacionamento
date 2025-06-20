from datetime import datetime, timedelta

def inferir_tipo_acesso(entrada: datetime, saida: datetime, horario_noturno_inicio: str, horario_noturno_fim: str) -> str:
    """
    Inferir o tipo de acesso com base na duração e horários.
    """
    duracao = saida - entrada
    horas = duracao.total_seconds() / 3600

    # Converter strings de horário para datetime.time
    noturno_inicio = datetime.strptime(horario_noturno_inicio, "%H:%M").time()
    noturno_fim = datetime.strptime(horario_noturno_fim, "%H:%M").time()

    # Verifica se a entrada e saída estão no intervalo noturno
    if entrada.time() >= noturno_inicio or saida.time() <= noturno_fim:
        return "noturno"
    elif horas >= 9:
        return "diaria"
    elif horas >= 1:
        return "hora_cheia"
    elif horas > 0:
        return "fracao"
    else:
        return "invalido"
