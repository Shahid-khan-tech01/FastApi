from fastapi import FastAPI, HTTPException ,UploadFile, File
from fastapi.staticfiles import StaticFiles
import os
import shutil


app = FastAPI()

# Step 01 : Ensure that uploaded folder exist :
Upload_dir = "uploads"
os.makedirs(Upload_dir, exist_ok=True)

# Step 02 - Static Files Set-up :
app.mount("/files",StaticFiles(directory=Upload_dir), name="files")

#Step 03 - Upload a file to API :
@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    file_path = os.path.join(Upload_dir,filename)

    if not filename:
        raise HTTPException(status_code=400, detail="File not Selected")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
        return {
            "message": "File Uploaded Successfully",
            "Filename": filename,
            "File_url": f"http://127.0.0.1:8000/files/{filename}" 
        }

# Step 04 - Get File url by API :
@app.get("/files/{filename}")
def get_file(filename: str):
    file_path = os.path.join(Upload_dir,filename)
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )
    return {
        "File_url": f"http://127.0.0.1:8000/files/{filename}"
    }

@app.get("/")
def home():
    return{
        "message": "File Uploaded Api is Running"
    }