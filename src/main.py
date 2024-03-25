from fastapi import FastAPI
from src.controllers.index import users_router

app = FastAPI()

app.include_router(users_router)