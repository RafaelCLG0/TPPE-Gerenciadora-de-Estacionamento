from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.database.session import get_db
from src.models.acesso import Acesso
from src.schemas.acesso import AcessoCreate, AcessoOut

router = APIRouter(prefix="/acessos", tags=["Acessos"])

@router.post("/", response_model=AcessoOut)
async def criar_acesso(acesso: AcessoCreate, db: AsyncSession = Depends(get_db)):
    novo = Acesso(**acesso.dict())
    db.add(novo)
    await db.commit()
    await db.refresh(novo)
    return novo
