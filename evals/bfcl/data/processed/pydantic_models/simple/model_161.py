# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:55:24+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class DetailLevel(Enum):
    basic = 'basic'
    detailed = 'detailed'


class CrimeStatuteLookup(BaseModel):
    jurisdiction: str = Field(
        ..., description='The jurisdiction to search in, usually a state or country.'
    )
    crime: str = Field(..., description='The crime to search for.')
    detail_level: Optional[DetailLevel] = Field(
        DetailLevel.basic,
        description="How detailed of a report to return. Optional, default is 'basic'.",
    )
