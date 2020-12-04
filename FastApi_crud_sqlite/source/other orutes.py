@router.post("/uploadfile/")
async def upload_file(files: List[UploadFile] = File(...)):
    for file in files:
        with open("receive.png", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    return FileResponse("src/templates/redirect_page.html")


@router.get("/uploadpage", response_class=HTMLResponse)
async def upload_page():
    # return HTMLResponse(content=content)
    return FileResponse("src/templates/upload_image.html")


@router.get("/last_pic")
async def stream():
    path = "receive.png"
    file_like = open(path, mode="rb")
    return StreamingResponse(file_like, media_type="image/png")