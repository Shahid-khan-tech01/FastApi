#import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts")

# data = response.json()
# print(data[:3])

from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# To get all data :
@app.get("/all")
def all_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return response.json()

# To get specific data by id :
@app.get("/post_id")
def id_data(post_id:int):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="data not found")
    return response.json()