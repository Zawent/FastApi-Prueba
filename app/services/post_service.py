from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate

def create_post(db: Session, post: PostCreate, user_id: int):
    new_post = Post(
        title=post.title,
        content=post.content,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
        user_id=user_id,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_posts(db: Session):
    return db.query(Post).all()

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def remove_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
    return post

def update_post(db: Session, post_id: int, post_data: PostCreate, user_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        return None
    if post.user_id != user_id:  # 🔒 Solo el dueño puede editar
        return "unauthorized"

    post.title = post_data.title
    post.content = post_data.content
    post.updated_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(post)
    return post