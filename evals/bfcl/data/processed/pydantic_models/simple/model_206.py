# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:55:56+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class Amenity(Enum):
    Tennis_Court = 'Tennis Court'
    Picnic_Area = 'Picnic Area'
    Playground = 'Playground'
    Running_Track = 'Running Track'


class ParksFindNearby(BaseModel):
    location: str = Field(..., description='The city and state, e.g. London, UK')
    amenities: Optional[List[Amenity]] = Field(
        [Amenity.Running_Track], description="Preferred amenities in park. Default is ['Running Track']"
    )