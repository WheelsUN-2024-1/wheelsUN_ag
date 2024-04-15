import strawberry
from typing import List, Any, NewType, Optional




JSON = strawberry.scalar(
    NewType("JSON", object),
    description="The `JSON` scalar type represents JSON values as specified by ECMA-404",
    serialize=lambda v: v,
    parse_value=lambda v: v,
)


@strawberry.type
class Prediction:
    description: str

@strawberry.type
class Trip:
    id: str
    route: JSON
    price: int
    vehicleId: int
    transactionIds: List[str]
    currentState: int
    waypoints: List[str]
    startingPoint: str
    endingPoint: str


@strawberry.input
class TripInput:
    startingPoint: str
    endingPoint: str
    price: int
    vehicleId: int
    currentState: int

@strawberry.input
class TripPassenger:
    transactionId: int
    waypoint: str

@strawberry.input
class TransactionID:
    transactionId: int


@strawberry.input
class TripPatch:
    price: Optional[int] = None
    vehicleId: Optional[int] = None
    currentState: Optional[int] = None
    
    