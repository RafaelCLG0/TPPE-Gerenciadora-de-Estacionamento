from src.database import SessionLocal
from src.usuario.repository import Usuario
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_integracao_criar_usuario_e_verificar_banco():
    db = SessionLocal()
    try:
        client.post("/usuarios/", json={
            "nome": "Cliente",
            "email": "cliente@example.com",
            "senha": "1234",
            "perfil": "CLIENTE"
        })

        usuario = db.query(Usuario).filter(Usuario.email == "cliente@example.com").first()
        assert usuario is not None
        assert usuario.nome == "Cliente"
        assert usuario.perfil == "CLIENTE"
    finally:
        db.close()
