from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, Date, Time, Boolean, ForeignKey, Float
from src.database import Base
from datetime import datetime
from src.acesso.schema import AcessoCreate
from src.estacionamento.repository import Estacionamento
from src.acesso.inferencia import inferir_tipo_acesso

class Acesso(Base):
    __tablename__ = "acessos"

    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String(10))
    data_entrada = Column(Date)
    hora_entrada = Column(Time)
    data_saida = Column(Date)
    hora_saida = Column(Time)
    evento = Column(Boolean, default=False)
    mensalista = Column(Boolean, default=False)
    estacionamento_id = Column(Integer, ForeignKey("estacionamentos.id"))
    tipo_acesso = Column(String(20))
    valor_pago = Column(Float)

def criar_acesso(db: Session, acesso: AcessoCreate):
    estacionamento = db.query(Estacionamento).filter(Estacionamento.id == acesso.estacionamento_id).first()
    if not estacionamento:
        raise Exception("Estacionamento não encontrado")

    entrada_dt = datetime.combine(acesso.data_entrada, acesso.hora_entrada)
    saida_dt = datetime.combine(acesso.data_saida, acesso.hora_saida)

    # Lógica de cálculo
    if acesso.evento:
        valor = estacionamento.valorEvento
        tipo = "evento"
    elif acesso.mensalista:
        valor = estacionamento.valorMensalista
        tipo = "mensalista"
    else:
        tipo = inferir_tipo_acesso(entrada_dt, saida_dt, estacionamento.horarioNoturnoInicio, estacionamento.horarioNoturnoFim)
        duracao = saida_dt - entrada_dt
        minutos = duracao.total_seconds() / 60

        if tipo == "fracao":
            fracoes = (minutos + 14) // 15  # Arredonda para cima a cada 15 min
            valor = fracoes * estacionamento.valorFracao
        elif tipo == "hora_cheia":
            horas = (minutos + 59) // 60
            valor = horas * estacionamento.valorHoraCheia
        elif tipo == "diaria":
            valor = estacionamento.valorDiaria
        elif tipo == "noturno":
            valor = estacionamento.valorNoturno
        else:
            valor = 0.0

    novo_acesso = Acesso(**acesso.model_dump(), tipo_acesso=tipo, valor_pago=valor)
    db.add(novo_acesso)
    db.commit()
    db.refresh(novo_acesso)
    return novo_acesso

def listar_acessos(db: Session):
    return db.query(Acesso).all()
