def calcular_valor(tipo: str, estacionamento: dict) -> float:
    match tipo:
        case "mensalista":
            return estacionamento.get("taxa_mensal", 0)
        case "evento":
            return estacionamento.get("taxa_evento", 0)
        case "noturno":
            return estacionamento.get("taxa_noturno", 0)
        case "diaria":
            return estacionamento.get("taxa_diaria", 0)
        case "fracao":
            return estacionamento.get("descricao_hora", 0)
        case "hora":
            return estacionamento.get("valor_hora", 0)
        case _:
            return 0
