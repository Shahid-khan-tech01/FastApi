from fastapi import FastAPI, Request, Response
import time

app = FastAPI()

# middleware is a function that runs before and after each request :

# @app.middleware("http")
# async def log_request(request: Request, call_next):
#    print("Request received")
#    response = await call_next(request)
#    print("Request processed")
#    return response

# middleware loggging is a function that runs before and after each request,
#  it can be used to log the processing time of each request.

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Path {request.url.path}  | processing time: {process_time} seconds")
    return response