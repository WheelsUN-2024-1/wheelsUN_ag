
import requests
import json
import strawberry
from src.conn.transaction_ms import create_creditcard
from src.conn.users_ms import get_passenger_by_id


def create_card(id, creditcard):

    userInfo = get_passenger_by_id(id)
    creditcard.userId = userInfo.id
    creditcard.name = userInfo.userName

    creditCardResponse = create_creditcard(creditcard)

    return creditCardResponse