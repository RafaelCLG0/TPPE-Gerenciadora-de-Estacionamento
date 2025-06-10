def inferir_tipo_acesso(hora_entrada: int, hora_saida: int, evento: bool, mensalista: bool) -> str:
    duracao = hora_saida - hora_entrada
    if mensalista:
        return "mensalista"
    if evento:
        return "evento"
    if hora_entrada >= 21 or hora_saida <= 6:
        return "noturno"
    if duracao <= 15:
        return "fracao"
    if duracao <= 60:
        return "hora"
    if duracao > 720:
        return "diaria"
    return "hora"
