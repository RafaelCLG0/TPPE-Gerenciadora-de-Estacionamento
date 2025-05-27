from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src.core.config import settings

engine = create_async_engine(
    settings.sqlalchemy_database_url,
    echo=True,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

async def get_db():
    async with SessionLocal() as session:
        yield session
