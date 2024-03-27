import strawberry
from typing import Optional
@strawberry.type
class Vehicle_model:
    vehicleOwnerId: int
    vehiclePlate: str
    vehicleBrand: str
    vehicleModel: str
    vehicleCylinder: str 
    vehicleYear: int
    vehicleSeatingCapacity: int


@strawberry.input
class Vehicle_input(Vehicle_model):
    ...

@strawberry.input
class Vehicle_patch:
    vehicleOwnerId: Optional[int] = None
    vehiclePlate: Optional[str] = None
    vehicleBrand: Optional[str] = None
    vehicleModel: Optional[str] = None
    vehicleCylinder: Optional[str] = None 
    vehicleYear: Optional[int] = None
    vehicleSeatingCapacity: Optional[int] = None

