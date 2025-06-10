from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from src.models.base import Base
from src.models.acesso import Acesso

class Estacionamento(Base):
    __tablename__ = "estacionamentos"

    id = Column(Integer, primary_key=True, index=True)
    tipo_estacionamento = Column(String(50))
    descricao_hora = Column(Float)
    taxa_diaria = Column(Integer)
    taxa_evento = Column(Integer)
    contratante = Column(Float)
    taxa_noturno = Column(Float)
    taxa_mensal = Column(Float)
    valor_hora = Column(Float)
    hora_inicial = Column(Integer)
    hora_final = Column(Integer)
    capacidade = Column(Integer)

    acessos = relationship("Acesso", back_populates="estacionamento")

    def registrar_acesso(self, acesso: Acesso):
        self.acessos.append(acesso)
