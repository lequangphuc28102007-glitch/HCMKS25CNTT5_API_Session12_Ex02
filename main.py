from fastapi import FastAPI

from database import engine, Base
from routers import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Learning Document API")

app.include_router(router)