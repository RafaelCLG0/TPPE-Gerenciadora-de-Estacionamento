"""Módulo de relatórios: acessos por estacionamento e cálculo de repasses."""

from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func, and_

from src.database import SessionLocal
from src.acesso.repository import Acesso
from src.estacionamento.repository import Estacionamento
from src.relatorios.repository import Relatorio
from src.relatorios.schema import RelatorioOut

router = APIRouter()

def get_db():
    """Fornece uma sessão de banco de dados para uso nos endpoints."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/acessos-por-estacionamento/")
def acessos_por_estacionamento(db: Session = Depends(get_db)):
    """Retorna o total de acessos agrupado por estacionamento."""
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
    fim: datetime = Query(...),
    estacionamento_id: Optional[int] = Query(None) # Parâmetro opcional adicionado
):
    """
    Calcula o valor bruto, repasse e lucro para um período e, opcionalmente,
    para um estacionamento específico.
    """
    # Filtro base por período de tempo
    query_filter = and_(Acesso.data_saida >= inicio.date(), Acesso.data_saida <= fim.date())

    # Adiciona o filtro de estacionamento se um ID for fornecido
    if estacionamento_id:
        query_filter = and_(query_filter, Acesso.estacionamento_id == estacionamento_id)

    acessos_no_periodo = db.query(Acesso).filter(query_filter).all()

    if not acessos_no_periodo:
        return []

    resumo_financeiro = {}

    for acesso in acessos_no_periodo:
        estacionamento = db.query(Estacionamento).get(acesso.estacionamento_id)
        if not estacionamento:
            continue

        nome = estacionamento.nome
        if nome not in resumo_financeiro:
            resumo_financeiro[nome] = {
                "estacionamento_id": estacionamento.id,
                "total_bruto": 0.0,
                "total_repasse": 0.0,
                "lucro_liquido": 0.0,
            }

        valor_pago = acesso.valor_pago
        repasse = valor_pago * (estacionamento.percentualRepasse / 100)
        lucro = valor_pago - repasse

        resumo_financeiro[nome]["total_bruto"] += valor_pago
        resumo_financeiro[nome]["total_repasse"] += repasse
        resumo_financeiro[nome]["lucro_liquido"] += lucro

    # Salva os relatórios no banco
    for resumo in resumo_financeiro.values():
        relatorio = Relatorio(
            estacionamento_id=resumo["estacionamento_id"],
            valor_bruto=round(resumo["total_bruto"], 2),
            valor_repasse=round(resumo["total_repasse"], 2),
            valor_lucro=round(resumo["lucro_liquido"], 2),
        )
        db.add(relatorio)

    db.commit()

    return [
        {
            "estacionamento": nome,
            "total_bruto": round(resumo["total_bruto"], 2),
            "total_repasse": round(resumo["total_repasse"], 2),
            "lucro_liquido": round(resumo["lucro_liquido"], 2),
        }
        for nome, resumo in resumo_financeiro.items()
    ]


@router.get("/relatorios-salvos/", response_model=list[RelatorioOut])
def listar_relatorios(db: Session = Depends(get_db)):
    """Lista todos os relatórios financeiros salvos no banco."""
    relatorios = db.query(Relatorio).all()
    return relatorios


@router.delete("/relatorios/{relatorio_id}")
def deletar_relatorio(relatorio_id: int, db: Session = Depends(get_db)):
    """Remove um relatório específico do banco de dados pelo ID."""
    relatorio = db.query(Relatorio).filter(Relatorio.id == relatorio_id).first()
    if not relatorio:
        return {"detail": "Relatório não encontrado"}
    db.delete(relatorio)
    db.commit()
    return {"detail": "Relatório removido com sucesso"}
