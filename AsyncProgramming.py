import time
import asyncio 
from fastapi import FastAPI 


app = FastAPI()

# Synchronization is step by step process and waiting to complete 1st step :
# def task():
#     time.sleep(3)
#     return "done"

# Async doesn't wait for other processes :
@app.get("/")
async def tasks():
    await asyncio.sleep(3)
    return {"message":"Async done"}