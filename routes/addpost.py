from fastapi import FastAPI, HTTPException, Depends
from ..database import SessionLocal, engine
from ..models import Post
from typing import Annotated 
from sqlalchemy.orm import Session 
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins
)

class PostBase(BaseModel):
    postTitle:  str
    message: str
    created_at: str

class PostModel(PostBase):
    postId: int

    class Config:
        orm_mode = True


# call db and close
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_ependency = Annotated[Session, Depends(get_db)]

Post.metadata.create_all(bind=engine)
# Routers

@app.post("/posts/", response_model=PostModel)
async def create_post(post: PostBase, db: db_ependency):
    db_post = Post(**post.dict())
    db.add(db_post)
    db.commit()
    return db_post