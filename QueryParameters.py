from fastapi import FastAPI

app = FastAPI()

# Query Parameters
# for output : /user?name=John
@app.get("/user")
def user(name):
    return {"Name": name}

# Optional Query Parameters
# for output : /products?limits=200 by default limits is 10
@app.get("/products")
def products(limits: int = 10):
    return {"Limits": limits}

# Default Query Parameters
# for output : /items?name=Book&price=20
@app.get("/items")
def items(name: str = None, price: int = 10):
    return {"Name": name, 
    "Price": price
    }