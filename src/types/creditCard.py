import strawberry
import typing
from src.conn.transaction_ms import get_creditcard_by_id, create_creditcard, update_creditcard
from src.models.transactions import CreditCard_model, CreditCard_Response, CreditCard_patch
from strawberry.types import Info

@strawberry.type
class CreditCardQuery:
   
    @strawberry.field
    def creditCardByID(self, info: Info, id:int)->CreditCard_Response:
        return get_creditcard_by_id(id)
    
@strawberry.type
class CreditCardMutation :
    @strawberry.mutation
    def create_creditcard(self, info: Info, creditcard:CreditCard_model)->CreditCard_Response:        
        return create_creditcard(creditcard)
    
    @strawberry.mutation
    def updateCreditCard(self, info, id:int, creditcard:CreditCard_patch)->CreditCard_Response:
        return update_creditcard(id, creditcard)