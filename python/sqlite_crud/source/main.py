from fastapi import FastAPI, APIRouter
from fastapi.responses import RedirectResponse
import uvicorn

from source.database_routes import db_router

app = FastAPI()
app.include_router(db_router, prefix="/customer", tags=["Customer CRUD"])

@app.get("/")
async def index():
    return RedirectResponse("/docs")