from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, Float
from src.database import Base
from src.seguradora.schema import SeguradoraCreate

class Seguradora(Base):
    __tablename__ = "seguradoras"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    documento_cliente = Column(String(20), unique=True)
    percentual_desconto = Column(Float)

def criar_seguradora(db: Session, seguradora: SeguradoraCreate):
    nova = Seguradora(**seguradora.model_dump())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

def listar_seguradoras(db: Session):
    return db.query(Seguradora).all()

def buscar_desconto(db: Session, documento_cliente: str) -> float:
    desconto = db.query(Seguradora).filter(Seguradora.documento_cliente == documento_cliente).first()
    return desconto.percentual_desconto if desconto else 0.0
