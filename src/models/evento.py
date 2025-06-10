from sqlalchemy import Column, Integer, String
from src.models.base import Base

class Evento(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    inicio_evento = Column(String(20))
    fim_evento = Column(String(20))
