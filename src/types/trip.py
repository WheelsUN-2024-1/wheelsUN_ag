import strawberry
import typing
from src.conn.trip_ms import get_trips, get_trip_by_id, create_trip, update_trip, add_passg_trip, remove_passg_trip, delete_trip
from src.models.trip import Trip
from strawberry.types import Info

@strawberry.type
class Query:
    #allDrivers: typing.List[Driver_model] = strawberry.field(resolver= get_data)
    @strawberry.field
    def allTrips(self, info: Info)->typing.List[Trip]:
        return get_trips()
   
    @strawberry.field
    def tripById(self, info: Info, id:int)->Trip:
        return get_trip_by_id(id)
