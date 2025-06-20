from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.seguradora.schema import SeguradoraCreate, SeguradoraOut
from src.seguradora.repository import criar_seguradora, listar_seguradoras
from src.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SeguradoraOut)
def criar(seguradora: SeguradoraCreate, db: Session = Depends(get_db)):
    return criar_seguradora(db, seguradora)

@router.get("/", response_model=list[SeguradoraOut])
def listar(db: Session = Depends(get_db)):
    return listar_seguradoras(db)
