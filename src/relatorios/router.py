"""Módulo de relatórios: acessos por estacionamento e cálculo de repasses."""

from datetime import datetime
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from src.database import SessionLocal
from src.acesso.repository import Acesso
from src.estacionamento.repository import Estacionamento
from src.relatorios.repository import Relatorio
from src.relatorios.schema import RelatorioOut

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
    Calcula o valor bruto, repasse e lucro por estacionamento dentro de um intervalo de tempo
    e salva o relatório no banco.
    """
    acessos = (
        db.query(Acesso)
        .filter(Acesso.data_entrada >= inicio.date(), Acesso.data_saida <= fim.date())
        .all()
    )

    resumo_financeiro = {}

    for acesso in acessos:
        estacionamento = db.query(Estacionamento).filter(
            Estacionamento.id == acesso.estacionamento_id
        ).first()
        if not estacionamento:
            continue

        valor_pago = acesso.valor_pago or 0.0
        repasse = valor_pago * (estacionamento.percentualRepasse / 100)
        lucro = valor_pago - repasse
        nome = estacionamento.nome

        if nome not in resumo_financeiro:
            resumo_financeiro[nome] = {
                "estacionamento_id": estacionamento.id,
                "total_bruto": 0.0,
                "total_repasse": 0.0,
                "lucro_liquido": 0.0
            }

        resumo_financeiro[nome]["total_bruto"] += valor_pago
        resumo_financeiro[nome]["total_repasse"] += repasse
        resumo_financeiro[nome]["lucro_liquido"] += lucro

    # Salva os relatórios no banco
    for nome, resumo in resumo_financeiro.items():
        relatorio = Relatorio(
            estacionamento_id=resumo["estacionamento_id"],
            valor_bruto=round(resumo["total_bruto"], 2),
            valor_repasse=round(resumo["total_repasse"], 2),
            valor_lucro=round(resumo["lucro_liquido"], 2)
        )
        db.add(relatorio)

    db.commit()

    return [
        {
            "estacionamento": nome,
            "total_bruto": round(resumo["total_bruto"], 2),
            "total_repasse": round(resumo["total_repasse"], 2),
            "lucro_liquido": round(resumo["lucro_liquido"], 2)
        }
        for nome, resumo in resumo_financeiro.items()
    ]


@router.get("/relatorios-salvos/", response_model=list[RelatorioOut])
def listar_relatorios(db: Session = Depends(get_db)):
    """
    Lista todos os relatórios financeiros salvos no banco.
    """
    relatorios = db.query(Relatorio).all()
    return relatorios


@router.delete("/relatorios/{relatorio_id}")
def deletar_relatorio(relatorio_id: int, db: Session = Depends(get_db)):
    """
    Remove um relatório específico do banco de dados pelo ID.
    """
    relatorio = db.query(Relatorio).filter(Relatorio.id == relatorio_id).first()

    if not relatorio:
        return {"mensagem": "Relatório não encontrado."}

    db.delete(relatorio)
    db.commit()
    return {"mensagem": f"Relatório {relatorio_id} removido com sucesso."}
