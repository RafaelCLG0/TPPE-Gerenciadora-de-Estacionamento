from pydantic import BaseModel, ConfigDict
from datetime import datetime

class AcessoCreate(BaseModel):
    placa: str
    entrada: datetime
    saida: datetime
    estacionamento_id: int

class AcessoOut(BaseModel):
    id: int
    placa: str
    entrada: datetime
    saida: datetime
    estacionamento_id: int
    tipo_acesso: str

    model_config = ConfigDict(from_attributes=True)
