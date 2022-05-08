# FASTAPI - Project

### Work in progress
- py  -3  -m venv venv
- venv\Scripts\activate.bat
- uvicorn main:app  --reload

# Timeline

## 2nd May, technically 3rd May as I am updating this post midnight
- Started off with the FastAPI project.
- Created a virtual environment.
- Imported FastAPI
- Path operation
- Get and Post methods
- HTTP requests and started testing API via Postman

## 3rd May
- Schema Validation with Pydantic -> imported the Pydantic module and BaseModel class
- CRUD Operations 
- ![CRUD Operations explanation](https://assets.website-files.com/5ff66329429d880392f6cba2/61c325278ba0dc1f5c550f27_CRUD%20acronym.png)
- Storing in Array -> tested out the get and create posts on Postman -> imported the random module with randrange variable.
- Gave each posts an ID. randrange was used for a random ID to be applied to create posts.
- Still learning at every step.

## 6th May
- Creating posts.
- Tested the Postman Collections & saving requests
- Retrieving
- Updating/changing response status codes (HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT, HTTP_201_CREATED)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- Deleting posts
- Imported Response, status, HTTPException

## 8th May
- Updating posts
- Created the "Update Post" under the project folder in Postman.
- all tests cleared
- Checked the FastAPI docs on Swagger UI http://127.0.0.1:8000/docs and Redoc http://127.0.0.1:8000/redoc
- Created a package and added a dummy file named __init__.py and moved the main.py file to the new folder named "app".
- all tests cleared in terminal and Postman
