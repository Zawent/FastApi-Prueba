from fastapi import FastAPI
from app.core.database import engine, Base
from app.routers import users
from app.routers import posts

app = FastAPI()

# Esto crea todas las tablas definidas en models
Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(posts.router)


@app.get("/")
def root():
    return {"message": "API con FastAPI y MySQL 🚀"}
