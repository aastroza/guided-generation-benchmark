# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:44:09+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class HotelBooking(BaseModel):
    hotel_name: str = Field(..., description='The name of the hotel.')
    location: str = Field(..., description='The city and state, e.g. New York, NY.')
    start_date: str = Field(
        ..., description="The start date of the reservation. Use format 'YYYY-MM-DD'."
    )
    end_date: str = Field(
        ..., description="The end date of the reservation. Use format 'YYYY-MM-DD'."
    )
    rooms: Optional[int] = Field(1, description='The number of rooms to reserve.')
