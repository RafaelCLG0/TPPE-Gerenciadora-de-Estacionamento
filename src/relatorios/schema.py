from pydantic import BaseModel
from datetime import datetime

class RelatorioOut(BaseModel):
    """
    Schema de saída para exibir o relatório financeiro.
    """
    estacionamento_id: int
    valor_bruto: float
    valor_repasse: float
    valor_lucro: float
    data_geracao: datetime
