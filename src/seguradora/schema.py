from pydantic import BaseModel, ConfigDict

class SeguradoraCreate(BaseModel):
    nome: str
    documento_cliente: str
    percentual_desconto: float

class SeguradoraOut(BaseModel):
    id: int
    nome: str
    documento_cliente: str
    percentual_desconto: float

    model_config = ConfigDict(from_attributes=True)
