from fastapi.testclient import TestClient
from src.models.usuario import Usuario
from src.db.connection import SessionLocal
from src.main import app
from src.core.security import hash_password


client = TestClient(app)


def garantir_admin():
    db = SessionLocal()
    try:
        email = "admin@test.com"
        usuario = db.query(Usuario).filter(Usuario.email == email).first()
        if not usuario:
            novo_usuario = Usuario(
                nome="Admin",
                email=email,
                senha_hash=hash_password("admin123"), 
                perfil="admin"
            )
            db.add(novo_usuario)
            db.commit()
    finally:
        db.close()



def get_token(email: str, senha: str) -> str:
    response = client.post("/auth/login", json={"email": email, "senha": senha})
    print("Resposta login:", response.status_code, response.text)
    if response.status_code == 200:
        return response.json()["access_token"]
    raise Exception("Falha ao obter token")