from fastapi import FastAPI, APIRouter
import uvicorn

app = FastAPI()


@app.get("/")
async def main():
    return {1}


if __name__ == "__main__":
    uvicorn.run("main:app", port=80, host="0.0.0.0", reload=True)
