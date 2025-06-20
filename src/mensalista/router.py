from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.mensalista.schema import MensalistaCreate, MensalistaOut
from src.mensalista.repository import criar_mensalista, listar_mensalistas
from src.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MensalistaOut)
def criar(mensalista: MensalistaCreate, db: Session = Depends(get_db)):
    return criar_mensalista(db, mensalista)

@router.get("/", response_model=list[MensalistaOut])
def listar(db: Session = Depends(get_db)):
    return listar_mensalistas(db)
