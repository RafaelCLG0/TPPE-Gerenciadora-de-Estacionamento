from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Acesso(Base):
    __tablename__ = "acessos"

    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String(10), nullable=False)
    tipo_acesso = Column(String(20), nullable=False)
    horario_entrada = Column(DateTime, default=datetime.utcnow)
    horario_saida = Column(DateTime, nullable=True)
