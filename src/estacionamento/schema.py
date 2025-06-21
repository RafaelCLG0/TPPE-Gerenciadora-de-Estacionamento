from pydantic import BaseModel, ConfigDict

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
    capacidade: int

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
    capacidade: int

    model_config = ConfigDict(from_attributes=True)
