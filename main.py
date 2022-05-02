from fastapi import FastAPI

app = FastAPI()

# Path operation


@app.get("/")  # decorator
def root():
    return {"message": "Hello world!"}
