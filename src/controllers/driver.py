import strawberry
from fastapi import APIRouter
from src.types.driver import Query, Mutation
from strawberry.asgi import GraphQL

driver_router = APIRouter()

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)

driver_router.add_route("/graphql", graphql_app)