from fastapi import FastAPI, APIRouter

db_router = APIRouter(prefix="/customer", tags=["customer"])


@db_router.post("/insert")
async def insert_new_customer():
    pass


@db_router.get("/search")
async def search_entry():
    pass


@db_router.get("/list")
async def insert_new_customer():
    pass


@db_router.put("/update")
async def update_customer():
    pass


@db_router.delete("/delete")
async def delete_customer():
    pass
