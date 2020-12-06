from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.responses import StreamingResponse
#import pythonMultipart
from fastapi.responses import RedirectResponse
import shutil
from typing import List
from PIL import Image
import PIL
import uvicorn


app = FastAPI()
path = "receive.png"


@app.post("/image/")
async def image(image: UploadFile = File(...)):
    with open("receive.png", "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    for file in files:
        with open("receive.png", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    return RedirectResponse("/home")


@app.get("/last_pic")
async def stream():
    file_like = open(path, mode="rb")
    return StreamingResponse(file_like, media_type="image/png")


@app.get("/")
async def index():
    return RedirectResponse("/home")


@app.get("/home")
async def main():
    content = """
<body>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file">
<input type="submit">
</form>
<img src=/last_pic alt="wait"/>
</body>"""
    return HTMLResponse(content=content)

if __name__ == '__main__':
    uvicorn.run("main:app", port=80, reload=True)
