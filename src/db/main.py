from sqlmodel import create_engine , text , SQLModel
# from sqlalchemy import create_engine
# from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from sqlalchemy.ext.asyncio import create_async_engine

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

