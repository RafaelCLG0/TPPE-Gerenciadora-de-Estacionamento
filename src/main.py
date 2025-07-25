"""Ponto de entrada da aplicação FastAPI para o sistema de gerenciamento de estacionamento."""

import time
from sqlalchemy.exc import OperationalError
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Imports do projeto
from src.database import Base, engine, DATABASE_URL
from src.usuario.router import router as usuario_router
from src.estacionamento.router import router as estacionamento_router
from src.acesso.router import router as acesso_router
from src.relatorios.router import router as relatorios_router

# Inicialização do app
app = FastAPI()

# =================================================================
# CONFIGURAÇÃO DE CORS (Cross-Origin Resource Sharing)
# =================================================================
origins = [
    "http://localhost",
    "http://localhost:8001",
    "http://127.0.0.1:5500",
    "https://gerenciadoradeestacionamento.netlify.app"  # URL de produção adicionada
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# =================================================================

print(f"DEBUG: Tentando conectar com a DATABASE_URL: {DATABASE_URL}")

# Aguarda o banco iniciar e cria as tabelas
MAX_RETRIES = 20
WAIT_SECONDS = 3
for attempt in range(MAX_RETRIES):
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Banco de dados conectado e tabelas criadas.")
        break
    except OperationalError as e:
        print(
            f"⏳ Tentativa {attempt + 1}/{MAX_RETRIES}: banco indisponível. "
            f"Tentando novamente em 3s... (Erro: {e})"
        )
        time.sleep(WAIT_SECONDS)
else:
    raise RuntimeError("❌ Não foi possível conectar ao banco de dados após várias tentativas.")

# =================================================================
# ROTA RAIZ (HEALTH CHECK)
# =================================================================
@app.get("/")
def health_check():
    """Endpoint raiz para verificação de saúde."""
    return {"status": "ok", "message": "API da Gerenciadora de Estacionamentos no ar!"}
# =================================================================

# Rotas
app.include_router(usuario_router, prefix="/usuarios", tags=["Usuários"])
app.include_router(estacionamento_router, prefix="/estacionamentos", tags=["Estacionamentos"])
app.include_router(acesso_router, prefix="/acessos", tags=["Acessos"])
app.include_router(relatorios_router, prefix="/relatorios", tags=["Relatórios"])
