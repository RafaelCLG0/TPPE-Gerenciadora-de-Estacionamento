from src.models.base import Base
from src.database.connection import engine

# Importa todos os modelos
from src.models import (
    estacionamento,
    acesso,
    evento,
    mensalista,
    turnos,
    horas_fracao,
    converter_tempo
)

def init_db():
    Base.metadata.create_all(bind=engine)
