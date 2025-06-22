"""Módulo de repositório para manipulação de usuários no sistema de turnos."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from src.database import Base
from src.usuario.schema import UsuarioCreate

class Usuario(Base):
    """
    Modelo ORM que representa um usuário no banco de dados.
    """
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    email = Column(String(100), unique=True)
    senha = Column(String(100))
    perfil = Column(String(50))

def criar_usuario(db: Session, usuario: UsuarioCreate):
    """
    Cria um novo usuário no banco de dados.
    """
    novo_usuario = Usuario(**usuario.model_dump())
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

def listar_usuarios(db: Session):
    """
    Retorna a lista de todos os usuários cadastrados.
    """
    return db.query(Usuario).all()
