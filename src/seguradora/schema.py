from pydantic import BaseModel

class SeguradoraCreate(BaseModel):
    nome: str
    documento_cliente: str
    percentual_desconto: float

class SeguradoraOut(BaseModel):
    id: int
    nome: str
    documento_cliente: str
    percentual_desconto: float

    class Config:
        orm_mode = True
