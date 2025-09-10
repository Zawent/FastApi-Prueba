from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.comment import CommentCreate, CommentResponse
from app.services import comment_service
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(prefix="/comments", tags=["Comments"])

@router.post("/post/{post_id}", response_model=CommentResponse, status_code=status.HTTP_201_CREATED)
def create_comment(
    post_id: int,
    comment: CommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return comment_service.create_comment(db, comment, current_user.id, post_id)

@router.get("/post/{post_id}", response_model=list[CommentResponse])
def list_comments(post_id: int, db: Session = Depends(get_db)):
    return comment_service.get_comments_by_post(db, post_id)

@router.put("/{comment_id}", response_model=CommentResponse)
def update_comment(
    comment_id: int,
    comment: CommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated = comment_service.update_comment(db, comment_id, comment, current_user.id)
    if updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
    if updated == "unauthorized":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to edit this comment")
    return updated

@router.delete("/{comment_id}", response_model=CommentResponse)
def delete_comment(
    comment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    deleted = comment_service.remove_comment(db, comment_id, current_user.id)
    if deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
    if deleted == "unauthorized":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this comment")
    return deleted
