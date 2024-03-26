from fastapi import FastAPI
from src.controllers.index import users_router
from src.controllers.index import trip_router

app = FastAPI()

app.include_router(users_router)
app.include_router(trip_router)