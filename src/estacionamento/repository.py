"""Módulo de repositório responsável pela manipulação de estacionamentos."""

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Session

from src.database import Base
from src.estacionamento.schema import EstacionamentoCreate

class Estacionamento(Base):
    """
    Modelo ORM que representa a tabela de estacionamentos.
    """
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
    """
    Cria e persiste um novo estacionamento no banco de dados.
    """
    novo_estacionamento = Estacionamento(**estacionamento.model_dump())
    db.add(novo_estacionamento)
    db.commit()
    db.refresh(novo_estacionamento)
    return novo_estacionamento

def listar_estacionamentos(db: Session):
    """
    Retorna a lista de todos os estacionamentos cadastrados.
    """
    return db.query(Estacionamento).all()
