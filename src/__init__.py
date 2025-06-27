from fastapi import FastAPI
from src.books.routes import book_router
from src.auth.routes import auth_router
from contextlib import asynccontextmanager 
from src.db.main import init_db

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"server đang bắt đầu")
    await init_db()
    yield
    print(f"server đã ngừng")

version = "v1"

app = FastAPI(
    title = "Bookly",
    description="A Rest Api for a book review web service",
    version=version,
    lifespan=life_span
)

app.include_router(book_router , prefix = f"/api/{version}/books" , tags = ['book'])
app.include_router(auth_router , prefix = f"/api/{version}/auth" , tags = ['auth'])
