"""Schemas Pydantic para operações com usuários."""

from pydantic import BaseModel, ConfigDict

class UsuarioCreate(BaseModel):
    """
    Schema de entrada para criação de um usuário.
    """
    nome: str
    email: str
    senha: str
    perfil: str

class UsuarioOut(BaseModel):
    """
    Schema de saída com os dados de um usuário.
    """
    id: int
    nome: str
    email: str
    perfil: str

    model_config = ConfigDict(from_attributes=True)
