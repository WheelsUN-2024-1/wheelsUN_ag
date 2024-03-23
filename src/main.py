from fastapi import FastAPI
from src.controllers.index import driver_router

app = FastAPI()

app.include_router(driver_router)