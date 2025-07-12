"""Configuração da conexão com o banco de dados e definição da base ORM."""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

# Define a URL do banco de dados para PostgreSQL.
# A string de conexão será montada a partir das variáveis de ambiente.
DB_USER = os.getenv("POSTGRES_USER", "admin")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "admin")
DB_HOST = os.getenv("DB_HOST", "db") # 'db' é o nome do serviço no docker-compose
DB_NAME = os.getenv("POSTGRES_DB", "estacionamento")
DB_PORT = os.getenv("DB_PORT", "5432")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# Cria a engine de conexão com o banco
engine = create_engine(DATABASE_URL)

# Sessão de banco utilizada nos endpoints
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos ORM
Base = declarative_base()
