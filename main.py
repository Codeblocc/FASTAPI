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


my_posts = [{"title": "title of post 1",
             "content": "content of of post 1", "id": 1}, {"title": "favourite NBA team", "content": "I am a fan of Boston Celtics", "id": 2}]


@app.get("/")  # decorator
def root():
    return {"message": "Welcome to my API!!!"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": post}
# title str, content str
