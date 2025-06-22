"""Schemas Pydantic para criação e retorno de acessos."""

from datetime import date, time
from pydantic import BaseModel, ConfigDict


class AcessoCreate(BaseModel):
    """
    Schema de entrada para criação de acesso.
    """
    placa: str
    data_entrada: date
    hora_entrada: time
    data_saida: date
    hora_saida: time
    evento: bool
    mensalista: bool
    estacionamento_id: int


class AcessoOut(BaseModel):
    """
    Schema de saída para exibição de acesso.
    """
    id: int
    placa: str
    data_entrada: date
    hora_entrada: time
    data_saida: date
    hora_saida: time
    evento: bool
    mensalista: bool
    estacionamento_id: int
    tipo_acesso: str
    valor_pago: float

    model_config = ConfigDict(from_attributes=True)
