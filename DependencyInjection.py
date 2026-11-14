from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

# Authorization:
def verify_token(token: str = Header(None)):
    if token != "1234":
        raise HTTPException(status_code=401, detail="Unauthorized User")
    return {"message": "Token verified successfully!"}

def name():
    return {
        "first_name": "Shahid",
        "last_name": "khan"
    }

# Dependency Injection means giving a function what it needs automatically.
#  In this case, the function name() is a dependency for the user() and dashboard() functions.

@app.get("/user")
def user(name = Depends(name)):
    return name

@app.get("/dashboard")
def dashboard(name = Depends(name)):
    return name

#Authorization intro: 
@app.get("/secure-dashboard")
def secure_dashboard(user = Depends(verify_token)):
    return {
        "message": "Welcome to the secure dashboard!",
        "User": user
        }