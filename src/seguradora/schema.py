"""Schemas Pydantic para criação e retorno de dados de seguradoras."""

from pydantic import BaseModel, ConfigDict

class SeguradoraCreate(BaseModel):
    """
    Schema de entrada para criação de uma nova seguradora.
    """
    nome: str
    documento_cliente: str
    percentual_desconto: float

class SeguradoraOut(BaseModel):
    """
    Schema de saída para exibição dos dados de uma seguradora.
    """
    id: int
    nome: str
    documento_cliente: str
    percentual_desconto: float

    model_config = ConfigDict(from_attributes=True)
