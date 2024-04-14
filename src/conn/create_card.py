
import requests
import json
import strawberry
from src.conn.transaction_ms import create_creditcard
from src.conn.users_ms import get_passenger_by_id
from src.models.transactions import CreditCard_model


def create_card(id, creditcard):

    userInfo = get_passenger_by_id(id)
    creditcardPost = {
        "CreditCardId": creditcard.CreditCardId,
        "UserId": id,
        "Number": creditcard.Number,
        "Name": userInfo.userName,
        "SecurityCode": creditcard.SecurityCode,
        "ExpirationDate": creditcard.ExpirationDate,
        "Brand": creditcard.Brand
    }
    
    creditCardResponse = create_creditcard(creditcardPost)

    return creditCardResponse