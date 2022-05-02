from fastapi import FastAPI

app = FastAPI()

# Path operation
# request Get method url: "/"


@app.get("/")  # decorator
def root():
    return {"message": "Welcome to my API!!!"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}
