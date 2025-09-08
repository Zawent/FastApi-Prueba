from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from passlib.context import CryptContext
from app.core.security import get_password_hash
from fastapi import HTTPException, status

# Configuración de passlib para bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 👉 función para hashear contraseñas
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# 👉 función para verificar contraseñas
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Crear usuario con contraseña hasheada
def create_user(db: Session, user: UserCreate):
    existing_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)
    ).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nombre de usuario ya registrado"
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
# Obtener todos los usuarios
def get_users(db: Session):
    return db.query(User).all()

# Obtener usuario por id
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# 👉 autenticar usuario (para login)
def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user
