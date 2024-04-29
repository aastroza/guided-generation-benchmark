# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:41:59+00:00

from __future__ import annotations

from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class Facility(Enum):
    Wi_Fi = 'Wi-Fi'
    Reading_Room = 'Reading Room'
    Fiction = 'Fiction'
    Children_Section = 'Children Section'
    Cafe = 'Cafe'


class PublicLibraryFindNearby(BaseModel):
    location: str = Field(..., description='The city and state, e.g. Boston, MA')
    facilities: List[Facility] = Field(
        ..., description='Facilities and sections in public library.'
    )
