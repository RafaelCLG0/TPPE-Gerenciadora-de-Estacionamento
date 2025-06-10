from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.acesso import AcessoCreate, AcessoResponse
from src.models import acesso as model
from src.models import estacionamento as estacionamento_model
from src.database.connection import SessionLocal

router = APIRouter(prefix="/acessos", tags=["Acessos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AcessoResponse)
def criar_acesso(acesso: AcessoCreate, db: Session = Depends(get_db)):
    estacionamento = db.query(estacionamento_model.Estacionamento).filter_by(id=acesso.estacionamento_id).first()
    if not estacionamento:
        raise HTTPException(status_code=404, detail="Estacionamento não encontrado")

    db_acesso = model.Acesso(**acesso.dict())
    valor = db_acesso.calcular_valor(estacionamento)
    db.add(db_acesso)
    db.commit()
    db.refresh(db_acesso)

    print(f"Tipo de acesso inferido: {db_acesso.inferir_tipo()} - Valor calculado: R$ {valor:.2f}")
    return db_acesso

@router.get("/", response_model=list[AcessoResponse])
def listar_acessos(db: Session = Depends(get_db)):
    return db.query(model.Acesso).all()

@router.put("/{id}", response_model=AcessoResponse)
def atualizar_acesso(id: int, acesso: AcessoCreate, db: Session = Depends(get_db)):
    db_acesso = db.query(model.Acesso).filter(model.Acesso.id == id).first()
    if not db_acesso:
        raise HTTPException(status_code=404, detail="Acesso não encontrado")
    for key, value in acesso.dict().items():
        setattr(db_acesso, key, value)
    db.commit()
    db.refresh(db_acesso)
    return db_acesso

@router.delete("/{id}")
def deletar_acesso(id: int, db: Session = Depends(get_db)):
    acesso = db.query(model.Acesso).filter(model.Acesso.id == id).first()
    if not acesso:
        raise HTTPException(status_code=404, detail="Acesso não encontrado")
    db.delete(acesso)
    db.commit()
    return {"mensagem": "Acesso removido com sucesso"}
