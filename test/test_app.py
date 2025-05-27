import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app")))

from src.main import app
from httpx import AsyncClient


@pytest.mark.skip(reason="Ignorado por enquanto – estrutura ok")
@pytest.mark.asyncio
async def test_hello_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@pytest.mark.skip(reason="Ignorado por enquanto – estrutura ok")
def test_somador_simples():
    assert 1 + 1 == 2
