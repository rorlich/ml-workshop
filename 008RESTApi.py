from fastapi import FastAPI, Query

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, File, Form, UploadFile

origins = [
    "http://localhost:3000",  # React app is running on this URL
    "https://ds-recorder.validit.ai",
    # support all subdomains of ngrok-free.app
    "https://3a65-2a06-c701-4ca8-cf00-f54c-102-930d-713e.ngrok-free.app",
    "https://b11f-85-65-195-199.ngrok-free.app",
    # "http://localhost:8080", # You can add other origins as needed
]

app = FastAPI()

# Add middleware to allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of origins that can access the server
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/ping")
async def ping(text: str = Query(None)):
    response_text = text + " pong!" if text else "pong!"
    return {"ping": response_text}

# Include routers from the routers module
@app.post("/detect_human")
async def detect_human(file: UploadFile = File(...), file_name: str = Form('image.png')):
    content = await file.read()
    
    with open(file_name, 'wb') as f:
        f.write(content)

    return {"is_human": True }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
