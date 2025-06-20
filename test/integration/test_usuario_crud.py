import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.core.security import hash_password
from src.db.connection import SessionLocal
from src.models.usuario import Usuario


client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_admin():
    db = SessionLocal()
    db.query(Usuario).delete()
    admin = Usuario(
        nome="Admin Teste",
        email="admin@test.com",
        senha_hash=hash_password("admin123"),
        perfil="admin"
    )
    db.add(admin)
    db.commit()
    db.close()

def get_token(email, senha):
    response = client.post("/auth/login", json={"email": email, "senha": senha})
    print("Login response:", response.status_code, response.text)
    return response.json().get("access_token")

def test_criar_usuario():
    token = get_token("admin@test.com", "admin123")
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "nome": "Usuário Teste",
        "email": "user@test.com",
        "senha": "user123",
        "perfil": "cliente"
    }
    r = client.post("/usuarios/", json=payload, headers=headers)
    assert r.status_code == 200
    assert r.json()["email"] == "user@test.com"

def test_listar_usuarios():
    token = get_token("admin@test.com", "admin123")
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/usuarios/", headers=headers)
    assert response.status_code == 200

def test_obter_usuario_por_id():
    token = get_token("admin@test.com", "admin123")
    headers = {"Authorization": f"Bearer {token}"}
    users = client.get("/usuarios/", headers=headers).json()
    assert isinstance(users, list) and users, "Nenhum usuário retornado"
    user_id = users[0]["id"]
    r = client.get(f"/usuarios/{user_id}", headers=headers)
    assert r.status_code == 200
    assert "email" in r.json()

def test_atualizar_usuario():
    token = get_token("admin@test.com", "admin123")
    headers = {"Authorization": f"Bearer {token}"}
    users = client.get("/usuarios/", headers=headers).json()
    assert isinstance(users, list) and users, "Nenhum usuário retornado"
    user_id = users[0]["id"]
    r = client.put(
        f"/usuarios/{user_id}",
        json={
            "nome": "Atualizado",
            "email": users[0]["email"],
            "senha": "admin123",
            "perfil": users[0]["perfil"]
        },
        headers=headers
    )
    assert r.status_code == 200
    assert r.json()["nome"] == "Atualizado"

def test_deletar_usuario():
    token = get_token("admin@test.com", "admin123")
    headers = {"Authorization": f"Bearer {token}"}
    users = client.get("/usuarios/", headers=headers).json()
    assert isinstance(users, list) and users, "Nenhum usuário retornado"
    user_id = users[-1]["id"]
    r = client.delete(f"/usuarios/{user_id}", headers=headers)
    assert r.status_code in [200, 204]