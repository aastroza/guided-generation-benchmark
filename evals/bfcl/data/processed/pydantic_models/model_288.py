# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:42:57+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class ConcertBookingBookTicket(BaseModel):
    artist: str = Field(..., description='The artist you want to book tickets for.')
    city: str = Field(..., description='The city where the concert is.')
    num_tickets: Optional[int] = Field(
        None, description='Number of tickets required. Default is 1.'
    )
