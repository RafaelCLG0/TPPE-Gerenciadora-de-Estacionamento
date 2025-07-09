"""Ponto de entrada da aplicação FastAPI para o sistema de gerenciamento de estacionamento."""

import time
from sqlalchemy.exc import OperationalError
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Importar o middleware de CORS

# Imports do projeto
from src.database import Base, engine
from src.usuario.router import router as usuario_router
from src.estacionamento.router import router as estacionamento_router
from src.acesso.router import router as acesso_router
from src.relatorios.router import router as relatorios_router

# Inicialização do app
app = FastAPI()

# =================================================================
# CONFIGURAÇÃO DE CORS (Cross-Origin Resource Sharing)
# =================================================================
# Esta seção permite que o front-end (rodando em um servidor de desenvolvimento
# como http://localhost:8001 ou http://127.0.0.1:5500) se comunique com a API.
origins = [
    "http://localhost",
    "http://localhost:8001",
    "http://localhost:5500",
    "http://127.0.0.1",
    "http://127.0.0.1:8001",
    "http://127.0.0.1:5500",
    "null" # Adicionado para permitir testes locais com file://, embora não seja o ideal.
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)
# =================================================================

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
