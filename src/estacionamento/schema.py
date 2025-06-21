from pydantic import BaseModel, ConfigDict
from typing import Optional

class EstacionamentoCreate(BaseModel):
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

class EstacionamentoOut(BaseModel):
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

    model_config = ConfigDict(from_attributes=True)
