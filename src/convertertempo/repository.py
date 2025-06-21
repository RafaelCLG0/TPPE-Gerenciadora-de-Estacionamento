from sqlalchemy.orm import Session
from src.usuario.schema import UsuarioCreate
from src.database import Base
from sqlalchemy import Column, Integer, String

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    email = Column(String(100), unique=True)
    senha = Column(String(100))
    perfil = Column(String(50))

def criar_usuario(db: Session, usuario: UsuarioCreate):
    novo_usuario = Usuario(**usuario.model_dump())
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

def listar_usuarios(db: Session):
    return db.query(Usuario).all()
