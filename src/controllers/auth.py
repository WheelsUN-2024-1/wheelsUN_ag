import strawberry
from fastapi import APIRouter
from src.types.auth import AuthMutation, Query
from strawberry.asgi import GraphQL


auth_router = APIRouter()


@strawberry.type
class Query(Query):
    ...    
#here we combine all mutations
@strawberry.type
class Mutation(AuthMutation):
    ...



schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)


auth_router.add_route("/auth", graphql_app)
