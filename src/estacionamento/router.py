"""Módulo de rotas para operações de CRUD com estacionamentos."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.estacionamento.schema import EstacionamentoCreate, EstacionamentoOut
from src.estacionamento.repository import (
    criar_estacionamento,
    listar_estacionamentos,
    Estacionamento as EstacionamentoModel,
)
from src.database import SessionLocal

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

@router.post("/", response_model=EstacionamentoOut)
def criar(estacionamento: EstacionamentoCreate, db: Session = Depends(get_db)):
    """
    Cria um novo estacionamento.
    """
    return criar_estacionamento(db, estacionamento)

@router.get("/", response_model=list[EstacionamentoOut])
def listar(db: Session = Depends(get_db)):
    """
    Lista todos os estacionamentos cadastrados.
    """
    return listar_estacionamentos(db)

@router.put("/{estacionamento_id}", response_model=EstacionamentoOut)
def atualizar(estacionamento_id: int, estacionamento: EstacionamentoCreate, db: Session = Depends(get_db)):
    """
    Atualiza os dados de um estacionamento existente.
    """
    db_est = db.query(EstacionamentoModel).filter(EstacionamentoModel.id == estacionamento_id).first()
    if not db_est:
        raise HTTPException(status_code=404, detail="Estacionamento não encontrado")
    for key, value in estacionamento.model_dump().items():
        setattr(db_est, key, value)
    db.commit()
    db.refresh(db_est)
    return db_est

@router.delete("/{estacionamento_id}")
def remover(estacionamento_id: int, db: Session = Depends(get_db)):
    """
    Remove um estacionamento com base no ID.
    """
    db_est = db.query(EstacionamentoModel).filter(EstacionamentoModel.id == estacionamento_id).first()
    if not db_est:
        raise HTTPException(status_code=404, detail="Estacionamento não encontrado")
    db.delete(db_est)
    db.commit()
    return {"mensagem": "Estacionamento removido com sucesso"}
