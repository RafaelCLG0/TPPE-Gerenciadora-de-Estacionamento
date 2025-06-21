from pydantic import BaseModel, ConfigDict
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

    model_config = ConfigDict(from_attributes=True)
