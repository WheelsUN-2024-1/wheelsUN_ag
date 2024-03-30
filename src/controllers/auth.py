import strawberry
from fastapi import APIRouter
from src.types.auth import AuthMutation
from strawberry.asgi import GraphQL


auth_router = APIRouter()

    
#here we combine all mutations
@strawberry.type
class Mutation(AuthMutation):
    ...

schema = strawberry.Schema(Mutation)
graphql_app = GraphQL(schema)


auth_router.add_route("/auth", graphql_app)