"""Módulo de relatórios: acessos por estacionamento e cálculo de repasses."""

from datetime import datetime

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func

from src.database import SessionLocal
from src.acesso.repository import Acesso
from src.estacionamento.repository import Estacionamento

router = APIRouter()


def get_db():
    """
    Fornece uma sessão de banco de dados para uso nos endpoints.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/acessos-por-estacionamento/")
def acessos_por_estacionamento(db: Session = Depends(get_db)):
    """
    Retorna o total de acessos agrupado por estacionamento.
    """
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
    """
    Calcula o valor de repasse por estacionamento dentro de um intervalo de tempo.
    """
    acessos = (
        db.query(Acesso)
        .filter(Acesso.entrada >= inicio, Acesso.saida <= fim)
        .all()
    )

    total_repasses = {}
    for acesso in acessos:
        estacionamento = db.query(Estacionamento).filter(
            Estacionamento.id == acesso.estacionamento_id
        ).first()
        if not estacionamento:
            continue
        valor_simulado = 10.0  # Substituir por acesso.valor_pago se existir
        repasse = valor_simulado * (estacionamento.percentualRepasse / 100)
        nome = estacionamento.nome
        if nome not in total_repasses:
            total_repasses[nome] = 0
        total_repasses[nome] += repasse

    return [
        {"estacionamento": nome, "total_repasse": total}
        for nome, total in total_repasses.items()
    ]
