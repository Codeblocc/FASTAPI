from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randrange

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


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


@app.get("/")  # decorator
def root():
    return {"message": "Welcome to my API!!!"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}")  # path parameter
def get_post(id: int):  # this will convert the id to an integer

    post = find_post(id)
    print(post)
    return{"post_detail": post}
