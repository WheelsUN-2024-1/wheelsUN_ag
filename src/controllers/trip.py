import strawberry
from fastapi import APIRouter
from src.types.trip import TripQuery, TripMutation
from strawberry.asgi import GraphQL

trip_router = APIRouter()

#hwew we combine all querys
@strawberry.type
class Query(TripQuery):
    ...

#hwew we combine all mutations
@strawberry.type
class Mutation(TripMutation):
    ...


schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)

trip_router.add_route("/trip", graphql_app)