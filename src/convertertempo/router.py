"""Módulo de rotas para operações relacionadas a usuários."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.usuario.schema import UsuarioCreate, UsuarioOut
from src.usuario.repository import criar_usuario, listar_usuarios
from src.database import SessionLocal

router = APIRouter()

def get_db():
    """
    Obtém uma sessão de banco de dados para ser usada nos endpoints.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UsuarioOut)
def criar(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    """
    Cria um novo usuário.
    """
    return criar_usuario(db, usuario)

@router.get("/", response_model=list[UsuarioOut])
def listar(db: Session = Depends(get_db)):
    """
    Lista todos os usuários cadastrados.
    """
    return listar_usuarios(db)
