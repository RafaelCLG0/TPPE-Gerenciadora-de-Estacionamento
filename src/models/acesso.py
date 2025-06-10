from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base import Base

class Acesso(Base):
    __tablename__ = "acessos"

    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String(10), index=True)
    hora_entrada = Column(Integer)
    hora_saida = Column(Integer)
    data_entrada = Column(DateTime)
    data_saida = Column(DateTime)
    evento = Column(Boolean, default=False)
    mensalista = Column(Boolean, default=False)
    estacionamento_id = Column(Integer, ForeignKey("estacionamentos.id"))

    estacionamento = relationship("Estacionamento", back_populates="acessos")

    def inferir_tipo(self) -> str:
        duracao = self.hora_saida - self.hora_entrada
        if self.mensalista:
            return "mensalista"
        if self.evento:
            return "evento"
        if self.hora_entrada >= 21 or self.hora_saida <= 6:
            return "noturno"
        if duracao <= 15:
            return "fracao"
        if duracao <= 60:
            return "hora"
        if duracao > 720:
            return "diaria"
        return "hora"

    def calcular_valor(self, estacionamento) -> float:
        tipo = self.inferir_tipo()
        match tipo:
            case "mensalista":
                return estacionamento.taxa_mensal
            case "evento":
                return estacionamento.taxa_evento
            case "noturno":
                return estacionamento.taxa_noturno
            case "diaria":
                return estacionamento.taxa_diaria
            case "fracao":
                return estacionamento.descricao_hora
            case "hora":
                return estacionamento.valor_hora
            case _:
                return 0.0
