from fastapi import FastAPI, status, HTTPException


app = FastAPI()

# HTTP status codes are used to indicate the result of an HTTP request. (Hyper Text Transfer Protocol):
@app.post("/user", status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "User created successfully!"
        }

# Custom response with a different status code :
@app.get("/user")
def get_user():     
    return {
        "status": "success",
        "message": "User retrieved successfully!",
        "data": {
            "name": "John Doe",
            "age": 30
        }
    }

# Error handling with status codes:
@app.get("/user/{user_id}")
def get_user(user: int):
    if user != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return {
        "id": user,
        "name": "Shahid khan",
        "age": 30
    }