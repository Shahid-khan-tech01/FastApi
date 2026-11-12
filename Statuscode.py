from fastapi import FastAPI, status

app = FastAPI()

@app.get("/user", status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "User created successfully!"
        }
