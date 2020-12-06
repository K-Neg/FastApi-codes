from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse

some_file_path = "video.mp4"
app = FastAPI()


@app.get("/")
async def main():
    return FileResponse(some_file_path)

@app.get("/b")
def main():
    file_like = open(some_file_path, mode="rb")
    return StreamingResponse(file_like, media_type="video/mp4")