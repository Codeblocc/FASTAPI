from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel


app = FastAPI()

# Path operation
# request Get method url: "/"


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")  # decorator
def root():
    return {"message": "Welcome to my API!!!"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}


@app.post("/createposts")
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": post}
# title str, content str
