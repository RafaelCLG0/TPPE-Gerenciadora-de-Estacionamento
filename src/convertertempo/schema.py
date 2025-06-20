from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str
    perfil: str

class UsuarioOut(BaseModel):
    id: int
    nome: str
    email: str
    perfil: str

    class Config:
        orm_mode = True
