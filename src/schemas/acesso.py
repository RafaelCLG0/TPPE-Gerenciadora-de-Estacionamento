from datetime import datetime
from pydantic import BaseModel
from pydantic import ConfigDict

class AcessoBase(BaseModel):
    placa: str
    tipo_acesso: str
    horario_entrada: datetime
    horario_saida: datetime | None = None

class AcessoCreate(AcessoBase):
    pass

class AcessoOut(AcessoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
