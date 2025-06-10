from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.estacionamento import EstacionamentoCreate, EstacionamentoResponse
from src.models import estacionamento as model
from src.database.connection import SessionLocal

router = APIRouter(prefix="/estacionamentos", tags=["Estacionamentos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EstacionamentoResponse)
def criar_estacionamento(estacionamento: EstacionamentoCreate, db: Session = Depends(get_db)):
    db_estacionamento = model.Estacionamento(**estacionamento.dict())
    db.add(db_estacionamento)
    db.commit()
    db.refresh(db_estacionamento)
    return db_estacionamento

@router.get("/", response_model=list[EstacionamentoResponse])
def listar_estacionamentos(db: Session = Depends(get_db)):
    return db.query(model.Estacionamento).all()

@router.put("/{id}", response_model=EstacionamentoResponse)
def atualizar_estacionamento(id: int, estacionamento: EstacionamentoCreate, db: Session = Depends(get_db)):
    db_estacionamento = db.query(model.Estacionamento).filter(model.Estacionamento.id == id).first()
    if not db_estacionamento:
        raise HTTPException(status_code=404, detail="Estacionamento não encontrado")
    for key, value in estacionamento.dict().items():
        setattr(db_estacionamento, key, value)
    db.commit()
    db.refresh(db_estacionamento)
    return db_estacionamento

@router.delete("/{id}")
def deletar_estacionamento(id: int, db: Session = Depends(get_db)):
    estacionamento = db.query(model.Estacionamento).filter(model.Estacionamento.id == id).first()
    if not estacionamento:
        raise HTTPException(status_code=404, detail="Estacionamento não encontrado")
    db.delete(estacionamento)
    db.commit()
    return {"mensagem": "Estacionamento removido com sucesso"}
