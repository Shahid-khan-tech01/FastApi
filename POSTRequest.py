from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class User(BaseModel):
    username: str
    age: int
    password: str

@app.post("/create_user")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "data": user
    }
