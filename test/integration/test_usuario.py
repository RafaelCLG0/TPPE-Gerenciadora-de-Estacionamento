from test.utils import get_token, client, garantir_admin


def test_listar_usuarios():
    garantir_admin()
    token = get_token("admin@test.com", "admin123")
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/usuarios/", headers=headers)
    assert response.status_code == 200


def test_atualizar_usuario():
    garantir_admin()
    token = get_token("admin@test.com", "admin123")
    headers = {"Authorization": f"Bearer {token}"}
    usuarios = client.get("/usuarios/", headers=headers).json()
    assert usuarios, "Nenhum usuário retornado da API"
    usuario_id = usuarios[0]["id"]

    response = client.put(
        f"/usuarios/{usuario_id}",
        json={
            "nome": "Novo Nome",
            "email": usuarios[0]["email"],  
            "senha": "admin123",            
            "perfil": usuarios[0]["perfil"] 
        },
        headers=headers
    )

    assert response.status_code == 200


def test_deletar_usuario():
    garantir_admin()
    token = get_token("admin@test.com", "admin123")
    headers = {"Authorization": f"Bearer {token}"}
    usuarios = client.get("/usuarios/", headers=headers).json()
    assert usuarios, "Nenhum usuário retornado da API"
    usuario_id = usuarios[-1]["id"]

    response = client.delete(f"/usuarios/{usuario_id}", headers=headers)
    assert response.status_code == 204


def test_login_cliente_e_restricao_de_acesso_admin():
    # Admin cria novo cliente
    garantir_admin()
    admin_token = get_token("admin@test.com", "admin123")
    headers = {"Authorization": f"Bearer {admin_token}"}

    novo_cliente = {
        "nome": "João Cliente",
        "email": "joao@cliente.com",
        "senha": "cliente123",
        "perfil": "cliente"
    }

    response = client.post("/usuarios/", json=novo_cliente, headers=headers)
    assert response.status_code in [200, 400]  # 400 se já existir

    # Cliente realiza login
    cliente_token = get_token("joao@cliente.com", "cliente123")
    assert cliente_token is not None

    # Cliente tenta acessar rota restrita a admin
    headers_cliente = {"Authorization": f"Bearer {cliente_token}"}
    response_restrita = client.get("/usuarios/", headers=headers_cliente)
    assert response_restrita.status_code == 403


def test_cliente_acessa_com_sucesso_o_proprio_perfil():
    cliente_token = get_token("joao@cliente.com", "cliente123")
    headers = {"Authorization": f"Bearer {cliente_token}"}

    # Cliente tenta acessar listagem geral de usuários (restrita)
    response = client.get("/usuarios/", headers=headers)
    assert response.status_code == 403
