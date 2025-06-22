"""Configuração da conexão com o banco de dados e definição da base ORM."""

import os  # Import padrão vem antes de terceiros

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

# Define a URL do banco de dados, com fallback para padrão local
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:password@db/estacionamento")

# Cria a engine de conexão com o banco
engine = create_engine(DATABASE_URL)

# Sessão de banco utilizada nos endpoints
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos ORM
Base = declarative_base()
