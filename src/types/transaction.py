import strawberry
import typing
from src.conn.transaction_ms import get_transaction_by_id, create_transaction, create_transaction_database
from src.models.transactions import  Transaction_model, Transaction_Response, Transaction_database
from strawberry.types import Info

@strawberry.type
class TransactionQuery:   
    @strawberry.field
    def transactionById(self, info: Info, id:str)->Transaction_Response:
        return get_transaction_by_id(id)


@strawberry.type
class TransactionMutation:
    @strawberry.mutation
    def createTransaction(self, info: Info, transaction: Transaction_model)->Transaction_Response:
        return create_transaction(transaction)
    
    @strawberry.mutation
    def createTransactionDatabase(self, info: Info, transaction: Transaction_database)->None:
        return create_transaction_database(transaction)