from fastapi import FastAPI
from src.api.routers import router
from src.database.init_db import init_db

app = FastAPI(
    title="Sistema de Gerenciamento de Estacionamento",
    version="1.0.0"
)

init_db()  # Cria as tabelas automaticamente ao iniciar
app.include_router(router)
