from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from src.database import Base
from src.evento.schema import EventoCreate

class Evento(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String(10))
    entrada = Column(DateTime)
    saida = Column(DateTime)
    valor_fixo = Column(Float)
    estacionamento_id = Column(Integer, ForeignKey("estacionamentos.id"))

def criar_evento(db: Session, evento: EventoCreate):
    novo_evento = Evento(**evento.dict())
    db.add(novo_evento)
    db.commit()
    db.refresh(novo_evento)
    return novo_evento

def listar_eventos(db: Session):
    return db.query(Evento).all()
