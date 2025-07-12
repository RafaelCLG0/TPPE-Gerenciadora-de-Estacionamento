"""Módulo de rotas para operações de CRUD com estacionamentos."""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import Response
from sqlalchemy.orm import Session

from src.estacionamento.schema import EstacionamentoCreate, EstacionamentoOut
from src.estacionamento.repository import (
    criar_estacionamento,
    listar_estacionamentos,
    Estacionamento as EstacionamentoModel,
)
# Importar os modelos de Acesso e Relatorio para poder deletá-los
from src.acesso.repository import Acesso as AcessoModel
from src.relatorios.repository import Relatorio as RelatorioModel
from src.database import SessionLocal

router = APIRouter()

def get_db():
    """Fornece uma sessão de banco de dados para uso nos endpoints."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EstacionamentoOut)
def criar(estacionamento: EstacionamentoCreate, db: Session = Depends(get_db)):
    """Cria um novo estacionamento."""
    return criar_estacionamento(db, estacionamento)

@router.get("/", response_model=list[EstacionamentoOut])
def listar(db: Session = Depends(get_db)):
    """Lista todos os estacionamentos cadastrados."""
    return listar_estacionamentos(db)

@router.put("/{estacionamento_id}", response_model=EstacionamentoOut)
def atualizar(
    estacionamento_id: int,
    estacionamento: EstacionamentoCreate,
    db: Session = Depends(get_db)
):
    """Atualiza os dados de um estacionamento existente."""
    db_est = (
        db.query(EstacionamentoModel)
        .filter(EstacionamentoModel.id == estacionamento_id)
        .first()
    )
    if not db_est:
        raise HTTPException(status_code=404, detail="Estacionamento não encontrado")

    for key, value in estacionamento.model_dump().items():
        setattr(db_est, key, value)

    db.commit()
    db.refresh(db_est)
    return db_est

# =================================================================
# FUNÇÃO DE REMOÇÃO CORRIGIDA
# =================================================================
@router.delete("/{estacionamento_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover(estacionamento_id: int, db: Session = Depends(get_db)):
    """
    Remove um estacionamento e todos os seus acessos e relatórios associados.
    """
    db_est = (
        db.query(EstacionamentoModel)
        .filter(EstacionamentoModel.id == estacionamento_id)
        .first()
    )
    if not db_est:
        raise HTTPException(status_code=404, detail="Estacionamento não encontrado")

    # 1. Deletar todos os relatórios associados
    db.query(RelatorioModel).filter(
        RelatorioModel.estacionamento_id == estacionamento_id
    ).delete(synchronize_session=False)

    # 2. Deletar todos os acessos associados
    db.query(AcessoModel).filter(
        AcessoModel.estacionamento_id == estacionamento_id
    ).delete(synchronize_session=False)

    # 3. Agora, deletar o estacionamento
    db.delete(db_est)

    # 4. Comitar todas as alterações no banco de dados
    db.commit()

    # Retorna uma resposta vazia com status 204, indicando sucesso.
    return Response(status_code=status.HTTP_204_NO_CONTENT)
