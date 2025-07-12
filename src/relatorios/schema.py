"""Módulo de schemas Pydantic para a entidade de Relatórios."""

from datetime import datetime
from pydantic import BaseModel

class RelatorioOut(BaseModel):
    """
    Schema de saída para exibir o relatório financeiro.
    """
    estacionamento_id: int
    valor_bruto: float
    valor_repasse: float
    valor_lucro: float
    data_geracao: datetime

    class Config:
        """Habilita o modo ORM para o schema Pydantic."""
        from_attributes = True
