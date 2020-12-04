from fastapi import FastAPI, APIRouter
import threading
import uvicorn

from database_routes import db_router
from file_routes import file_router

app = FastAPI()
app.include_router(db_router, prefix="/customer", tags=["customer"])
app.include_router(file_router, prefix="/file", tags=["file"])


@app.get("/")
async def main():
    return {threading.active_count()}


if __name__ == "__main__":
    uvicorn.run("main:app", port=80, host="0.0.0.0", reload=True)
