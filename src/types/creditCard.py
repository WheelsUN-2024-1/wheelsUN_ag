import strawberry
import typing
from src.conn.transaction_ms import get_creditcard_by_id, update_creditcard, delete_creditcard, get_creditcard_by_user
from src.conn.create_card import create_card
from src.models.transactions import CreditCard_model, CreditCard_Response, CreditCard_patch
from strawberry.types import Info

@strawberry.type
class CreditCardQuery:
   
    @strawberry.field
    def creditCardByID(self, info: Info, id:int)->CreditCard_Response:
        return get_creditcard_by_id(id)
    
    @strawberry.field
    def creditCardByUser(self, info: Info, id:int)->typing.List[CreditCard_Response]:
        return get_creditcard_by_user(id)
    
@strawberry.type
class CreditCardMutation :
    @strawberry.mutation
    def createCreditCard(self, info: Info, id:str, creditcard:CreditCard_model)->CreditCard_Response:        
        return create_card(id,creditcard)
    
    @strawberry.mutation
    def updateCreditCard(self, info, id:int, creditcard:CreditCard_patch)->CreditCard_Response:
        return update_creditcard(id, creditcard)
    
    @strawberry.mutation
    def deleteCreditCard(self, info, id:int)->CreditCard_Response:
        return delete_creditcard(id)