from fastapi import FastAPI
from src.api.v1.endpoints import acesso

app = FastAPI()

app.include_router(acesso.router)

@app.get("/ping-db")
async def ping_db():
    return {"status": "OK"}