from fastapi import FastAPI
from src.controllers.index import users_router
from src.controllers.index import trip_router
from src.controllers.index import transaction_router
from src.controllers.index import auth_router

#this is for test purposes---------------------------
from src.wheelsUN_mq.new_task import push_notification
from src.wheelsUN_mq.worker import main
#----------------------------------------------------

import asyncio

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(main())
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(users_router)
app.include_router(trip_router)
app.include_router(transaction_router)
app.include_router(auth_router)



#this is for test purposes---------------------------
@app.get("/rabbitmq/{message}")
async def rabbitmq(message:str):
    dict = {"message": message, "destination": "mail"}
    push_notification(dict)
    return "message pushed"




