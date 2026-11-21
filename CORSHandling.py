# CORS : Cross origin Resource Sharing 
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse


app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Display HTML Page
@app.get("/", response_class=HTMLResponse)
def home():
    with open("CORS.html") as file:
        return file.read()

# Receive HTML Form Data
@app.post("/submit", response_class=HTMLResponse)
def submit(name: str = Form(...)):
    return f"""
    <html>
        <body>
            <h1>Data Received Successfully</h1>
            <h3>Welcome {name}</h3>
        </body>
    </html>
    """