"""Ponto de entrada da aplicação FastAPI para o sistema de gerenciamento de estacionamento."""

import time  # Import padrão
from sqlalchemy.exc import OperationalError  # Import de terceiros

from fastapi import FastAPI  # Import de terceiros

# Imports do projeto
from src.database import Base, engine
from src.usuario.router import router as usuario_router
from src.estacionamento.router import router as estacionamento_router
from src.acesso.router import router as acesso_router
from src.relatorios.router import router as relatorios_router

# Inicialização do app
app = FastAPI()

# Aguarda o banco iniciar e cria as tabelas
MAX_RETRIES = 20
WAIT_SECONDS = 3
for attempt in range(MAX_RETRIES):
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Banco de dados conectado e tabelas criadas.")
        break
    except OperationalError:
        print(
            f"⏳ Tentativa {attempt + 1}/{MAX_RETRIES}: banco indisponível. "
            f"Tentando novamente em {WAIT_SECONDS}s..."
        )
        time.sleep(WAIT_SECONDS)
else:
    raise RuntimeError("❌ Não foi possível conectar ao banco de dados após várias tentativas.")

# Rotas
app.include_router(usuario_router, prefix="/usuarios", tags=["Usuários"])
app.include_router(estacionamento_router, prefix="/estacionamentos", tags=["Estacionamentos"])
app.include_router(acesso_router, prefix="/acessos", tags=["Acessos"])
app.include_router(relatorios_router, prefix="/relatorios", tags=["Relatórios"])
