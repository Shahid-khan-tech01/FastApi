from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# HTTP Exception usage :
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(
            status_code=123,
            detail="Jaake Id Check Karo"
        )
    return {
        "id": user_id,
        "name": "Shahid khan",
    }

# Custom Error Exception :
class UserNotFoundError(Exception):
    def __init__(self, name: str):
        self.name = name

@app.get("/name/{name}")
def get_name(name: str):
    if name != "Shahid":
        raise UserNotFoundError(name)
    return {
        "name": name,
        "age": 21,
    }

# Global Error Exception :
@app.exception_handler(UserNotFoundError)
def user_not_found_handler(request: Request, exc: UserNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "status_code": 404,
            "status": "error",
            "detail": f"User {exc.name} not found"
        }
    )
