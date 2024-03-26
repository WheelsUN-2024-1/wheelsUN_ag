import strawberry
from typing import List, Any, NewType




JSON = strawberry.scalar(
    NewType("JSON", object),
    description="The `JSON` scalar type represents JSON values as specified by ECMA-404",
    serialize=lambda v: v,
    parse_value=lambda v: v,
)


@strawberry.type
class Trip:
    id: str
    route: JSON
    price: int
    vehicleId: int
    transactionIds: List[int]
    currentState: int


@strawberry.input
class TripInput:
    startingPoint: str
    endingPoint: str
    price: int
    vehicleId: int
    currentState: int
