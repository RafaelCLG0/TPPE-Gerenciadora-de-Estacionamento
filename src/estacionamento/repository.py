from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, Float
from src.database import Base
from src.estacionamento.schema import EstacionamentoCreate

class Estacionamento(Base):
    __tablename__ = "estacionamentos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    cnpj = Column(String(20), unique=True)
    valorFracao = Column(Float)
    valorHoraCheia = Column(Float)
    valorDiaria = Column(Float)
    valorMensalista = Column(Float)
    valorEvento = Column(Float)
    valorNoturno = Column(Float)
    horarioNoturnoInicio = Column(String(5))
    horarioNoturnoFim = Column(String(5))
    percentualRepasse = Column(Float)
    capacidade = Column(Integer)

def criar_estacionamento(db: Session, estacionamento: EstacionamentoCreate):
    novo_estacionamento = Estacionamento(**estacionamento.model_dump())
    db.add(novo_estacionamento)
    db.commit()
    db.refresh(novo_estacionamento)
    return novo_estacionamento

def listar_estacionamentos(db: Session):
    return db.query(Estacionamento).all()
