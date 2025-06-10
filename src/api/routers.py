from fastapi import APIRouter
from src.api import estacionamento

router = APIRouter()

router.include_router(estacionamento.router)

from src.api import acesso
router.include_router(acesso.router)

from src.api import relatorios
router.include_router(relatorios.router)

from src.api import seguradora
router.include_router(seguradora.router)
