from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "This is the home page of the FastAPI application."}  

@app.get("/about")
def about():
    return {"message": "This is the about page of the FastAPI application."}  

@app.get("/user")
def user():
    return {"username": ["JohnDoe", "JaneSmith", "AliceJohnson"]}  
