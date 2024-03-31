from fastapi import FastAPI
from src.controllers.index import users_router
from src.controllers.index import trip_router
from src.controllers.index import transaction_router

#this is for test purposes---------------------------
from src.messaging.new_task import push_notification
from src.messaging.worker import main
#----------------------------------------------------

app = FastAPI()

app.include_router(users_router)
app.include_router(trip_router)
app.include_router(transaction_router)

#this is for test purposes---------------------------
@app.get("/rabbitmq/{message}")
async def rabbitmq(message:str):
    #dict = {"message": message}
    push_notification(message)
    return "message pushed"

@app.get("/rabbitmqget")
async def rabbitmqget():
    await main()
    return "message pushed"
#----------------------------------------------------