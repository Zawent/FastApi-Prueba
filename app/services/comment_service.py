from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.models.comment import Comment
from app.schemas.comment import CommentCreate

def create_comment(db: Session, comment: CommentCreate, user_id: int, post_id: int):
    new_comment = Comment(
        content=comment.content,
        user_id=user_id,
        post_id=post_id,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def get_comments_by_post(db: Session, post_id: int):
    return db.query(Comment).filter(Comment.post_id == post_id).all()

def get_comment(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()

def remove_comment(db: Session, comment_id: int, user_id: int):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        return None
    if comment.user_id != user_id:
        return "unauthorized"
    db.delete(comment)
    db.commit()
    return comment

def update_comment(db: Session, comment_id: int, comment_data: CommentCreate, user_id: int):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        return None
    if comment.user_id != user_id:
        return "unauthorized"
    comment.content = comment_data.content
    comment.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(comment)
    return comment
