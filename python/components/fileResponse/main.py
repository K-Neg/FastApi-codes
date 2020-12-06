from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse

some_file_path = "sample.mp4"
app = FastAPI()

@app.get("/")
def index():
    return {"Choose path /file or /stream"}

@app.get("/file")
async def direct_file():
    return FileResponse(some_file_path)

@app.get("/stream")
async def stream():
    file_like = open(some_file_path, mode="rb")
    return StreamingResponse(file_like, media_type="video/mp4")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app")