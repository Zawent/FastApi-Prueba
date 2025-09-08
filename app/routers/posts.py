from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.post import PostCreate, PostResponse
from app.services import post_service
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(
    post: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # ✅ Ahora viene del token
):
    return post_service.create_post(db, post, user_id=current_user.id)

@router.get("/", response_model=list[PostResponse])
def list_posts(db: Session = Depends(get_db)):
    return post_service.get_posts(db)

@router.get("/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = post_service.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

@router.delete("/{post_id}", response_model=PostResponse)
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # ✅ protege con token
):
    post = post_service.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    # Opcional: valida que el post sea del usuario logueado
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this post")

    return post_service.remove_post(db, post_id)
