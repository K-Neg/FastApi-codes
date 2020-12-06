from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import FileResponse

from typing import List

from source.schemas import OutputModel
from source.models import register_model

app = FastAPI()


@app.get("/")
def index():
    return FileResponse("source/index.html")


@app.post("/multipart-form/", response_model=OutputModel)
async def receive_data(
    files: List[UploadFile] = File(...),
    name: str = Form(...),
    code: int = Form(...),
):
    insertion = register_model(files, name, code)
    return {"name": insertion.name, "code": insertion.code, "avatar": insertion.avatar}
