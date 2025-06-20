from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.evento.schema import EventoCreate, EventoOut
from src.evento.repository import criar_evento, listar_eventos
from src.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EventoOut)
def criar(evento: EventoCreate, db: Session = Depends(get_db)):
    return criar_evento(db, evento)

@router.get("/", response_model=list[EventoOut])
def listar(db: Session = Depends(get_db)):
    return listar_eventos(db)
