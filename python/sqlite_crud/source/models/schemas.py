from pydantic import BaseModel, Field


class CustomerSchema(BaseModel):
    name: str = Field(...)
    age: int = Field(...)
    description: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                # "user_id": 1,
                "name": "George",
                "age": 25,
                "description": "Nice Guy",
            }
        }


class updateCustomerSchema(BaseModel):
    name: str = Field(...)
    age: int = Field(...)
    description: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Gandalf",
                "age": 3000,
                "description": "Long Hair",
            }
        }