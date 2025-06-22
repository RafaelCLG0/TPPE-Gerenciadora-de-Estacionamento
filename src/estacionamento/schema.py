"""Schemas Pydantic para entrada e saída de dados de estacionamento."""

from pydantic import BaseModel, ConfigDict

class EstacionamentoCreate(BaseModel):
    """
    Schema para criação de um novo estacionamento.
    """
    nome: str
    cnpj: str
    valorFracao: float
    valorHoraCheia: float
    valorDiaria: float
    valorMensalista: float
    valorEvento: float
    valorNoturno: float
    horarioNoturnoInicio: str
    horarioNoturnoFim: str
    percentualRepasse: float
    capacidade: int

class EstacionamentoOut(BaseModel):
    """
    Schema para exibição dos dados de um estacionamento.
    """
    id: int
    nome: str
    cnpj: str
    valorFracao: float
    valorHoraCheia: float
    valorDiaria: float
    valorMensalista: float
    valorEvento: float
    valorNoturno: float
    horarioNoturnoInicio: str
    horarioNoturnoFim: str
    percentualRepasse: float
    capacidade: int

    model_config = ConfigDict(from_attributes=True)
