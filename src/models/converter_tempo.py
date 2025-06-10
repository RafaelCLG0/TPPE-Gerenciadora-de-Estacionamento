from sqlalchemy import Column, Integer
from src.models.base import Base

class ConverterTempo(Base):
    __tablename__ = "converter_tempo"

    id = Column(Integer, primary_key=True, index=True)
    tempo_minuto = Column(Integer)

    def converter(self, hora_inicio: int, hora_fim: int) -> int:
        return (hora_fim - hora_inicio) * 60
