"""Repositório para operações com seguradoras."""

from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, Float
from src.database import Base
from src.seguradora.schema import SeguradoraCreate

class Seguradora(Base):
    """
    Modelo ORM que representa uma seguradora.
    """
    __tablename__ = "seguradoras"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    documento_cliente = Column(String(20), unique=True)
    percentual_desconto = Column(Float)

def criar_seguradora(db: Session, seguradora: SeguradoraCreate):
    """
    Cria e salva uma nova seguradora no banco de dados.
    """
    nova = Seguradora(**seguradora.model_dump())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

def listar_seguradoras(db: Session):
    """
    Retorna todas as seguradoras cadastradas.
    """
    return db.query(Seguradora).all()

def buscar_desconto(db: Session, documento_cliente: str) -> float:
    """
    Busca o percentual de desconto com base no documento do cliente.

    Retorna 0.0 caso nenhuma seguradora corresponda.
    """
    desconto = (
        db.query(Seguradora)
        .filter(Seguradora.documento_cliente == documento_cliente)
        .first()
    )
    return desconto.percentual_desconto if desconto else 0.0
