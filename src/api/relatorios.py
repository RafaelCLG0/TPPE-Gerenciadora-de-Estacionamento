from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.connection import SessionLocal
from src.models.acesso import Acesso
from sqlalchemy import func
from datetime import datetime

router = APIRouter(prefix="/relatorios", tags=["Relatórios"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/consolidado")
def relatorio_consolidado(db: Session = Depends(get_db)):
    total_acessos = db.query(func.count(Acesso.id)).scalar()
    return {"total_acessos": total_acessos}

@router.get("/repasses")
def calcular_repasses(db: Session = Depends(get_db), inicio: str = "", fim: str = ""):
    try:
        data_inicio = datetime.strptime(inicio, "%Y-%m-%d")
        data_fim = datetime.strptime(fim, "%Y-%m-%d")
    except ValueError:
        return {"erro": "Formato de data inválido. Use YYYY-MM-DD"}

    acessos_periodo = db.query(Acesso).filter(Acesso.data_entrada >= data_inicio, Acesso.data_saida <= data_fim).all()
    total_repasses = sum([a.estacionamento.contratante for a in acessos_periodo if a.estacionamento])
    return {"periodo": f"{inicio} a {fim}", "total_repasses": total_repasses}
