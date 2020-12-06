from pydantic import Schema, BaseModel
from typing import Optional


class ItemSchema(BaseModel):
    name: str
    code: int
    avatar: str

    class Config:
        schema_extra = {"example": {"name": "Mike", "code": 4, "avatar": "sample.png"}}


class OutputModel(BaseModel):
    name: Optional[str]
    code: int
    file_name: Optional[str]
