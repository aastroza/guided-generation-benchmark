# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:28+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Source(Enum):
    scriptures = 'scriptures'
    historical_records = 'historical records'


class GetEarliestReference(BaseModel):
    name: str = Field(..., description='The name of the person.')
    source: Optional[Source] = Field(
        Source.scriptures, description="Source to fetch the reference. Default is 'scriptures'"
    )
