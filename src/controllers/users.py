import strawberry
from fastapi import APIRouter
from src.types.driver import DriverQuery, DriverMutation
from src.types.passenger import PassengerQuery, PassengerMutation
from src.types.vehicle import VehicleQuery, VehicleMutation

from src.types.authentication import AuthenticationMutation
from src.types.auth import AuthMutation

from strawberry.asgi import GraphQL

users_router = APIRouter()

#here we combine all querys
@strawberry.type
class Query(DriverQuery, PassengerQuery, VehicleQuery):
    ...

#here we combine all mutations
@strawberry.type
class Mutation(DriverMutation, PassengerMutation, VehicleMutation, AuthenticationMutation, AuthMutation):
    ...

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)

users_router.add_route("/graphql", graphql_app)