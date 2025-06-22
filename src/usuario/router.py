"""Rotas para operações de criação e listagem de usuários."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.usuario.schema import UsuarioCreate, UsuarioOut
from src.usuario.repository import criar_usuario, listar_usuarios
from src.database import SessionLocal

router = APIRouter()

def get_db():
    """
    Fornece uma sessão de banco de dados para os endpoints.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UsuarioOut)
def criar(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    """
    Endpoint para criar um novo usuário.

    Parâmetros:
    - usuario: dados do novo usuário.
    - db: sessão do banco de dados.

    Retorna:
    - Usuário criado.
    """
    return criar_usuario(db, usuario)

@router.get("/", response_model=list[UsuarioOut])
def listar(db: Session = Depends(get_db)):
    """
    Endpoint para listar todos os usuários.

    Parâmetros:
    - db: sessão do banco de dados.

    Retorna:
    - Lista de usuários cadastrados.
    """
    return listar_usuarios(db)
