from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.database import Base
from src.acesso.schema import AcessoCreate
from src.acesso.inferencia import inferir_tipo_acesso
from src.estacionamento.repository import Estacionamento

class Acesso(Base):
    __tablename__ = "acessos"

    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String(10))
    entrada = Column(DateTime)
    saida = Column(DateTime)
    estacionamento_id = Column(Integer, ForeignKey("estacionamentos.id"))
    tipo_acesso = Column(String(20))

def criar_acesso(db: Session, acesso: AcessoCreate):
    estacionamento = db.query(Estacionamento).filter(Estacionamento.id == acesso.estacionamento_id).first()
    if not estacionamento:
        raise Exception("Estacionamento não encontrado")

    tipo = inferir_tipo_acesso(
        acesso.entrada,
        acesso.saida,
        estacionamento.horarioNoturnoInicio,
        estacionamento.horarioNoturnoFim
    )

    novo_acesso = Acesso(**acesso.model_dump(), tipo_acesso=tipo)
    db.add(novo_acesso)
    db.commit()
    db.refresh(novo_acesso)
    return novo_acesso

def listar_acessos(db: Session):
    return db.query(Acesso).all()
