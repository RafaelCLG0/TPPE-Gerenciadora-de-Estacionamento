"""Schemas Pydantic para criação e retorno de usuários."""

from pydantic import BaseModel, ConfigDict

class UsuarioCreate(BaseModel):
    """
    Schema de entrada para criação de usuário.
    """
    nome: str
    email: str
    senha: str
    perfil: str

class UsuarioOut(BaseModel):
    """
    Schema de saída para exibição de usuário.
    """
    id: int
    nome: str
    email: str
    perfil: str

    model_config = ConfigDict(from_attributes=True)
