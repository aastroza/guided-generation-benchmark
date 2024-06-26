# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:30+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class EventType(Enum):
    all = 'all'
    crusade = 'crusade'
    schism = 'schism'
    reform = 'reform'


class GetReligionHistory(BaseModel):
    religion: str = Field(..., description='The name of the religion.')
    start_year: int = Field(..., description='The starting year of the period.')
    end_year: int = Field(..., description='The end year of the period.')
    event_type: Optional[EventType] = Field(
        EventType.all,
        description="Optional parameter specifying the type of event. Default is 'all'.",
    )
