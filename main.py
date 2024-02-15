from contextlib import asynccontextmanager

from fastapi import FastAPI

from db import database
from resources.routes import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)
