from fastapi import FastAPI

app = FastAPI()

# For creating the dynamic routes 
# Add ? after the user_id to make it optional.
@app.get("/user/{user_id}")

# using of the path parameter as integer
def get_user(user_id: int):

# using of the path parameter as string
# def get_user(user_id: str):

# Here user_id is a path parameter that can be chnged dynamically.
    return {"user_id": user_id}