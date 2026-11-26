from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Shahid bro"}

@app.get("/add")
def Add(a:int, b:int):
    return {"result": a+b
            }