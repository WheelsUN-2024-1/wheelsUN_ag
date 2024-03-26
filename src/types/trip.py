import strawberry
import typing
from src.conn.trip_ms import get_trips, get_trip_by_id, create_trip, update_trip, add_passg_trip, remove_passg_trip, delete_trip
from src.models.trip import Trip, TripInput
from strawberry.types import Info

@strawberry.type
class TripQuery:
    @strawberry.field
    def allTrips(self, info: Info)->typing.List[Trip]:
        return get_trips()
   
    @strawberry.field
    def tripById(self, info: Info, id:str)->Trip:
        return get_trip_by_id(id)


@strawberry.type
class TripMutation:
    @strawberry.mutation
    def createTrip(self, info: Info, trip: TripInput)->Trip:        
        return create_trip(trip)
    