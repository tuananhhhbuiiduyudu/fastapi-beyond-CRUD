"""
Các bước thực hiện 1 dự án FastAPI
1. Xác định domain và chia module :
    - Ví dụ bài toán quản lý sách (books) , người dùng (auth) , quản lý database(db)
2. Tạo CSDL & Model 
    - Việc đầu tiên lên làm là model hóa dữ liệu , tức :
        models.py trong từng modul
        định nghĩa các lớp ORM (với SQLaichemy) đại diện cho bảng 
3. Tạo schemas (Pydantic models)
    - schemas.py (trong đừng model)
        Là các class để validate input/ouput
4. Tạo service logic 
    - Viết các hàm xử lý nghiệp vụ , gọi DB
5. Tạo routes (API enpoints)
    - router.py
6. Khởi tạo app & đăng router
    -main.py trong db
7.Cấu hình database 
    - config.py 

TỔNG KẾT
✅ Thứ tự triển khai gợi ý:
models.py → tạo ORM model.

schemas.py → tạo Pydantic schemas.

config.py & database.py → setup database.

service.py → viết business logic.

routes.py → định nghĩa API.

main.py → khởi tạo app, include router.

Sau cùng: test trên Swagger UI.
"""

# alembic init migrations	Tạo thư mục migration dùng sync
# alembic init -t async migrations	Tạo migration có hỗ trợ async DB (cho FastAPI + asyncpg)

# Mục đích	alembic revision --autogenerate -m "init" dùng để
# 🏗️	Tạo file migration tự động từ model Python
# 🧠	So sánh model và database, tìm sự khác biệt
# 📝	Sinh ra câu lệnh SQL để tạo hoặc thay đổi bảng

# alembic init -t async migrations
# 👉 Tạo cấu trúc thư mục hỗ trợ async

# Viết model Python (class kế thừa từ SQLModel hoặc Base)

# alembic revision --autogenerate -m "init"
# 👉 Tạo file migration tự động từ model

# ✅ alembic upgrade head
# 👉 Thực thi câu lệnh SQL tương ứng để tạo bảng, thêm cột... trong cơ sở dữ liệu PostgreSQL
from fastapi import FastAPI , Header
from typing import Optional 
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/greet/{name}")
async def greet_name(name: Optional[str] = "User", 
                     age:int=18 ) -> dict:
    return {"message": f"Hello {name}", "age" : age}

class BookCreateModel(BaseModel):
    title : str  
    author : str

@app.post('/create_book')
async def create_book(book_data : BookCreateModel):
    return {
        "title" : book_data.title ,
        "author" : book_data.author
    }

@app.get('/get_headers' , status_code=200)
async def get_headers(
    accept:str = Header(None),
    content_type : str = Header(None) ,
    user_agent : str = Header(None) , 
    host : str = Header(None)
):
    request_headers = {}
    
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host
    return request_headers
