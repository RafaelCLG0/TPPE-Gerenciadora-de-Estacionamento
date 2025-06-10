from sqlalchemy import Column, Integer
from src.models.base import Base

class Mensalista(Base):
    __tablename__ = "mensalistas"

    id = Column(Integer, primary_key=True, index=True)
    valor_mensal = Column(Integer)
