from pydantic import BaseModel

class EstacionamentoBase(BaseModel):
    tipo_estacionamento: str
    descricao_hora: float
    taxa_diaria: int
    taxa_evento: int
    contratante: float
    taxa_noturno: float
    taxa_mensal: float
    valor_hora: float
    hora_inicial: int
    hora_final: int
    capacidade: int

class EstacionamentoCreate(EstacionamentoBase):
    pass

class EstacionamentoResponse(EstacionamentoBase):
    id: int

    class Config:
        orm_mode = True
