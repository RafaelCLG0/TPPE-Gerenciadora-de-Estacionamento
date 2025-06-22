"""Funções de persistência e manipulação de dados dos usuários."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from src.database import Base
from src.usuario.schema import UsuarioCreate

class Usuario(Base):
    """
    Modelo ORM para representar usuários no banco de dados.
    """
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    email = Column(String(100), unique=True)
    senha = Column(String(100))
    perfil = Column(String(50))

def criar_usuario(db: Session, usuario: UsuarioCreate):
    """
    Cria um novo usuário a partir dos dados recebidos e persiste no banco.
    
    Parâmetros:
    - db (Session): Sessão ativa do banco de dados.
    - usuario (UsuarioCreate): Dados do usuário a ser criado.

    Retorna:
    - Usuario: Objeto do usuário criado.
    """
    novo_usuario = Usuario(**usuario.model_dump())
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

def listar_usuarios(db: Session):
    """
    Retorna todos os usuários cadastrados no sistema.

    Parâmetros:
    - db (Session): Sessão ativa do banco de dados.

    Retorna:
    - list[Usuario]: Lista de usuários.
    """
    return db.query(Usuario).all()
