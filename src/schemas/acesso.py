from pydantic import BaseModel
from datetime import datetime

class AcessoBase(BaseModel):
    placa: str
    hora_entrada: int
    hora_saida: int
    data_entrada: datetime
    data_saida: datetime
    evento: bool = False
    mensalista: bool = False
    estacionamento_id: int

class AcessoCreate(AcessoBase):
    pass

class AcessoResponse(AcessoBase):
    id: int

    class Config:
        orm_mode = True
