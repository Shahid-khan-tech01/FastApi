# Pydantic Models in FastAPI

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Creating a simple Pydantic model for user data:
# class User(BaseModel):
#   username: str
#   age: int
# @app.post("/create_user")
# def create_user(user: User):
#    return {
#       "message": "User created successfully",
#       "user": user
#    }

# Nested Pydantic models :

class Address(BaseModel):
    city: str
    pin_code: int

class User(BaseModel):
    username: str
    age: int
    address: Address

@app.post("/create_user")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "user": user
    }