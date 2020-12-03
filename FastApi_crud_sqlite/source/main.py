from fastapi import FastAPI, APIRouter
import uvicorn

from database_routes import db_router

app = FastAPI()
app.include_router(db_router)


@app.get("/")
async def main():
    return {1}


if __name__ == "__main__":
    uvicorn.run("main:app", port=80, host="0.0.0.0", reload=True)
