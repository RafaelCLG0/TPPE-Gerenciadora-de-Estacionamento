from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.connection import SessionLocal
from src.models.acesso import Acesso
from src.models.estacionamento import Estacionamento

router = APIRouter(prefix="/seguradora", tags=["Seguradora"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/aplicar-desconto/{acesso_id}")
def aplicar_desconto_global(acesso_id: int, desconto: float, db: Session = Depends(get_db)):
    acesso = db.query(Acesso).filter(Acesso.id == acesso_id).first()
    if not acesso:
        raise HTTPException(status_code=404, detail="Acesso não encontrado")

    estacionamento = db.query(Estacionamento).filter(Estacionamento.id == acesso.estacionamento_id).first()
    if not estacionamento:
        raise HTTPException(status_code=404, detail="Estacionamento não encontrado")

    valor_base = acesso.calcular_valor(estacionamento)
    valor_com_desconto = valor_base * (1 - desconto / 100)

    return {
        "acesso_id": acesso.id,
        "tipo": acesso.inferir_tipo(),
        "valor_base": valor_base,
        "desconto_aplicado": f"{desconto:.2f}%",
        "valor_final": round(valor_com_desconto, 2)
    }
