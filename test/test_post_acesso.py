import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_criar_acesso():
    async with AsyncClient(base_url="http://app:8000") as ac:
        payload = {
            "placa": "ABC1234",
            "tipo_acesso": "fração",
            "horario_entrada": "2025-05-27T13:00:00"
        }
        response = await ac.post("/acessos/", json=payload)
    assert response.status_code == 200
    assert response.json()["placa"] == "ABC1234"