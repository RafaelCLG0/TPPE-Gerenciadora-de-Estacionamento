from pydantic import BaseModel, ConfigDict
from datetime import date, time

class AcessoCreate(BaseModel):
    placa: str
    data_entrada: date
    hora_entrada: time
    data_saida: date
    hora_saida: time
    evento: bool
    mensalista: bool
    estacionamento_id: int

class AcessoOut(BaseModel):
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
