from pydantic import BaseModel
from datetime import date

class MensalistaCreate(BaseModel):
    nome: str
    cpf: str
    placa: str
    inicio_vigencia: date
    fim_vigencia: date
    estacionamento_id: int

class MensalistaOut(BaseModel):
    id: int
    nome: str
    cpf: str
    placa: str
    inicio_vigencia: date
    fim_vigencia: date
    estacionamento_id: int

    class Config:
        orm_mode = True
