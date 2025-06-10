from sqlalchemy import Column, Integer
from src.models.base import Base

class Turnos(Base):
    __tablename__ = "turnos"

    id = Column(Integer, primary_key=True, index=True)
    taxa_diaria = Column(Integer)
    taxa_noturno = Column(Integer)

    def verificar_noturno(self, hora_entrada: int, hora_saida: int) -> bool:
        return hora_entrada >= 21 or hora_saida <= 6
