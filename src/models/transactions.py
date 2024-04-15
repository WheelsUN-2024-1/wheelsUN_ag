import strawberry
from typing import List, Any, NewType
from typing import Optional

JSON = strawberry.scalar(
    NewType("JSON", object),
    description="The `JSON` scalar type represents JSON values as specified by ECMA-404",
    serialize=lambda v: v,
    parse_value=lambda v: v,
)

@strawberry.input
class CreditCard_model:
    CreditCardId: int
    UserId: int
    Number: str
    Name: str
    SecurityCode: str
    ExpirationDate: str
    Brand:str

@strawberry.type
class CreditCard_Response:
    ID : int
    CreatedAt: str
    UpdatedAt: str
    DeletedAt: str
    creditCardId: int
    userId: int
    number: str
    name: str
    securityCode: str
    expirationDate: str
    brand:str

@strawberry.input
class CreditCard_patch:
    CreditCardId: Optional[int] = None
    UserId: Optional[int] = None
    Number: Optional[str] = None
    Name: Optional[str] = None
    SecurityCode: Optional[str] = None
    ExpirationDate: Optional[str] = None
    BranD: Optional[str] = None

@strawberry.input
class Transaction_model:
    language : str
    command : str
    test : bool
    merchant : JSON
    transaction : JSON

@strawberry.input
class Transaction_database:
    referenceCode : str
    description : str
    value : int
    paymentMethods : str
    state : str
    tripId: int
    creditCardId:int

@strawberry.type
class Transaction_Response:
    ID : int
    CreatedAt: str
    UpdatedAt: str
    DeletedAt: str
    referenceCode : str
    description : str
    value : int
    paymentMethods : str
    state : str
    tripId: int
    creditCardId:int