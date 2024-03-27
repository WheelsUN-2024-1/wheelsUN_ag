import strawberry
from fastapi import APIRouter
from src.types.creditCard import CreditCardMutation, CreditCardQuery
from src.types.transaction import TransactionMutation, TransactionQuery
from strawberry.asgi import GraphQL


transaction_router = APIRouter()

#here we combine all querys
@strawberry.type
class Query(TransactionQuery, CreditCardQuery):
    ...

#here we combine all mutations
@strawberry.type
class Mutation(TransactionMutation, CreditCardMutation):
    ...

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)


transaction_router.add_route("/transaction", graphql_app)