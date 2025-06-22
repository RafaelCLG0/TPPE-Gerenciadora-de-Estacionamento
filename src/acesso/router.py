from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.acesso.schema import AcessoCreate, AcessoOut
from src.acesso.repository import (
    criar_acesso,
    listar_acessos,
    Acesso as AcessoModel,
)
from src.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AcessoOut)
def criar(acesso: AcessoCreate, db: Session = Depends(get_db)):
    """
    Cria um novo acesso no estacionamento.
    """
    acesso_criado = criar_acesso(db, acesso)
    return AcessoOut.model_validate(acesso_criado)

@router.get("/", response_model=list[AcessoOut])
def listar(db: Session = Depends(get_db)):
    """
    Lista todos os acessos registrados no sistema.
    """
    return listar_acessos(db)

@router.put("/{acesso_id}", response_model=AcessoOut)
def atualizar(acesso_id: int, acesso: AcessoCreate, db: Session = Depends(get_db)):
    """
    Atualiza um acesso existente com base no ID.
    """
    db_acesso = db.query(AcessoModel).filter(AcessoModel.id == acesso_id).first()
    if not db_acesso:
        raise HTTPException(status_code=404, detail="Acesso não encontrado")
    for key, value in acesso.model_dump().items():
        setattr(db_acesso, key, value)
    db.commit()
    db.refresh(db_acesso)
    return AcessoOut.model_validate(db_acesso)

@router.delete("/{acesso_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover(acesso_id: int, db: Session = Depends(get_db)):
    """
    Remove um acesso do sistema com base no ID.
    """
    db_acesso = db.query(AcessoModel).filter(AcessoModel.id == acesso_id).first()
    if not db_acesso:
        raise HTTPException(status_code=404, detail="Acesso não encontrado")
    db.delete(db_acesso)
    db.commit()
