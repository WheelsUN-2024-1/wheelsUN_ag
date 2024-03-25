import strawberry
from fastapi import APIRouter
from src.types.driver import DriverQuery, DriverMutation
from src.types.passenger import PassengerQuery, PassengerMutation
from strawberry.asgi import GraphQL

users_router = APIRouter()

#hwew we combine all querys
@strawberry.type
class Query(DriverQuery, PassengerQuery):
    ...

#hwew we combine all mutations
@strawberry.type
class Mutation(DriverMutation, PassengerMutation):
    ...

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)

users_router.add_route("/graphql", graphql_app)