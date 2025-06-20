from pydantic import BaseModel
from datetime import datetime

class EventoCreate(BaseModel):
    placa: str
    entrada: datetime
    saida: datetime
    valor_fixo: float
    estacionamento_id: int

class EventoOut(BaseModel):
    id: int
    placa: str
    entrada: datetime
    saida: datetime
    valor_fixo: float
    estacionamento_id: int

    class Config:
        orm_mode = True
