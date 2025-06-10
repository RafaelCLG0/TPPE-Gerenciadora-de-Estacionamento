from sqlalchemy import Column, Integer
from src.models.base import Base

class HorasFracao(Base):
    __tablename__ = "horas_fracao"

    id = Column(Integer, primary_key=True, index=True)
    tempo_minuto = Column(Integer)
