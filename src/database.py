"""Configuração da conexão com o banco de dados e definição da base ORM."""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env (útil para desenvolvimento local sem Docker)
load_dotenv()

# Prioriza a DATABASE_URL completa, que é fornecida pelo Render.
DATABASE_URL = os.getenv("DATABASE_URL")

# Se a DATABASE_URL não for encontrada no ambiente (como no Docker local ou no host),
# monta a URL a partir de partes.
if not DATABASE_URL:
    print("DEBUG: DATABASE_URL não encontrada, montando para ambiente local.")
    DB_USER = os.getenv("POSTGRES_USER", "admin")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "admin")
    DB_NAME = os.getenv("POSTGRES_DB", "estacionamento")
    
    # Esta lógica agora funciona para ambos os métodos de teste locais:
    # - Dentro do Docker (Método 2), as variáveis de ambiente serão usadas.
    # - No seu Mac (Método 1), os valores padrão (localhost:5433) serão usados.
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5433")
    
    DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
else:
    # O Render fornece uma URL no formato postgres://...
    # O SQLAlchemy 1.4+ recomenda usar postgresql://...
    # Esta linha garante a compatibilidade.
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    print("DEBUG: Usando DATABASE_URL do ambiente de produção.")


print(f"DEBUG: Tentando conectar com a DATABASE_URL: {DATABASE_URL}")

# Cria a engine de conexão com o banco
engine = create_engine(DATABASE_URL)

# Sessão de banco utilizada nos endpoints
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos ORM
Base = declarative_base()
