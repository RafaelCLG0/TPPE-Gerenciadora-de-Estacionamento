from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from src.database import Base
from datetime import datetime

class Relatorio(Base):
    """
    Modelo ORM para armazenar relatórios financeiros por estacionamento.
    """
    __tablename__ = "relatorios"

    id = Column(Integer, primary_key=True, index=True)
    estacionamento_id = Column(Integer, ForeignKey("estacionamentos.id"))
    valor_bruto = Column(Float)
    valor_repasse = Column(Float)
    valor_lucro = Column(Float)
    data_geracao = Column(DateTime, default=datetime.utcnow)
