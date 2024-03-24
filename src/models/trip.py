import strawberry
import typing


@strawberry.type
class Trip:
    id: int
    route: any
    price: int
    vehicleId: int
    transactionIds: any
    currentState: int
