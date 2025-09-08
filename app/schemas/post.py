from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass  # hereda todo de PostBase, no hace falta repetir

class PostResponse(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime
    user_id: int

    class Config:
        from_attributes = True  # equivalente a orm_mode=True en Pydantic v1
