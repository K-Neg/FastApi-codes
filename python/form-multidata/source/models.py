from source.schemas import ItemSchema
import shutil


def register_model(files, name, code):
    file_name = file_uploader(files, str(name) + str(code))
    new_item = ItemSchema(name=name, code=code, avatar=file_name)
    return new_item


def file_uploader(files, id):
    for file in files:
        file_name = "image_" + str(file.filename) + "_" + str(id) + ".png"
        with open(file_name, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    return file_name