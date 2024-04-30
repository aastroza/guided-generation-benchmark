# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:55:57+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class AvoidEnum(Enum):
    tolls = 'tolls'
    highways = 'highways'
    ferries = 'ferries'


class MapServiceGetDirections(BaseModel):
    start: str = Field(..., description='Starting location for the route.')
    end: str = Field(..., description='Ending location for the route.')
    avoid: Optional[List[AvoidEnum]] = Field(
        [AvoidEnum.highways, AvoidEnum.ferries], description="Route features to avoid. Default is ['highways', 'ferries']"
    )
