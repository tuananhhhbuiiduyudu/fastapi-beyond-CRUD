from sqlmodel import create_engine , text , SQLModel
# from sqlalchemy import create_engine
# from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
# from sqlmodel.ext.asyncio import AsyncSession
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker 
# engine = create_engine(
#      url = Config.DATABASE_URL,
#      echo = True
# )
engine = create_async_engine(
    Config.DATABASE_URL,
    echo=True
)

async def init_db():
    async with engine.begin() as conn : 
        from src.books.models import Book
        
        await conn.run_sync(SQLModel.metadata.create_all)
        
async def get_session()->AsyncSession:
    Session = sessionmaker(
        bind = engine , 
        class_ = AsyncSession, 
        expire_on_commit=False , 
    )
    
    async with Session() as session : 
        yield session

if __name__ == "__main__":
    asyncio.run(init_db())
# from sqlalchemy.ext.asyncio import create_async_engine
# from sqlmodel import text
# from src.config import Config

# print("Loaded DATABASE_URL from .env:", Config.DATABASE_URL)  # debug


# engine = create_async_engine(
#     Config.DATABASE_URL,
#     echo=True
# )

# async def init_db():
#     async with engine.begin() as conn:
#         result = await conn.execute(text("SELECT 'hello from local';"))
#         print(result.all())

