from fastapi import FastAPI
from app.core.database import engine, Base
from app.routers import users
from app.routers import posts
from app.routers import comment
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # tu front (Vite/React)
    allow_credentials=True,
    allow_methods=["*"],   # Permite GET, POST, PUT, DELETE, OPTIONS...
    allow_headers=["*"],   # Permite enviar Authorization, Content-Type, etc.
)
Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(comment.router)


@app.get("/")
def root():
    return {"message": "API con FastAPI y MySQL 🚀"}
