from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from src.database import Base
from src.mensalista.schema import MensalistaCreate

class Mensalista(Base):
    __tablename__ = "mensalistas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    cpf = Column(String(14), unique=True)
    placa = Column(String(10))
    inicio_vigencia = Column(Date)
    fim_vigencia = Column(Date)
    estacionamento_id = Column(Integer, ForeignKey("estacionamentos.id"))

def criar_mensalista(db: Session, mensalista: MensalistaCreate):
    novo_mensalista = Mensalista(**mensalista.dict())
    db.add(novo_mensalista)
    db.commit()
    db.refresh(novo_mensalista)
    return novo_mensalista

def listar_mensalistas(db: Session):
    return db.query(Mensalista).all()
