from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import SessionLocal
from src.acesso.repository import Acesso
from src.estacionamento.repository import Estacionamento
from datetime import datetime
from fastapi import Query
from sqlalchemy import func

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/acessos-por-estacionamento/")
def acessos_por_estacionamento(db: Session = Depends(get_db)):
    resultados = (
        db.query(Estacionamento.nome, func.count(Acesso.id).label("total_acessos"))
        .join(Acesso, Acesso.estacionamento_id == Estacionamento.id)
        .group_by(Estacionamento.nome)
        .all()
    )
    return [{"estacionamento": nome, "total_acessos": total} for nome, total in resultados]

@router.get("/repasses/")
def calcular_repasses(
    db: Session = Depends(get_db),
    inicio: datetime = Query(...),
    fim: datetime = Query(...)
):
    acessos = db.query(Acesso).filter(Acesso.entrada >= inicio, Acesso.saida <= fim).all()
    total_repasses = {}

    for acesso in acessos:
        estacionamento = db.query(Estacionamento).filter(Estacionamento.id == acesso.estacionamento_id).first()
        if not estacionamento:
            continue
        # Simulação de valor de acesso, poderia ser lido de acesso.valor_cobrado se existir
        valor_simulado = 10.0
        repasse = valor_simulado * (estacionamento.percentualRepasse / 100)
        nome = estacionamento.nome
        if nome not in total_repasses:
            total_repasses[nome] = 0
        total_repasses[nome] += repasse

    return [{"estacionamento": nome, "total_repasse": total} for nome, total in total_repasses.items()]
