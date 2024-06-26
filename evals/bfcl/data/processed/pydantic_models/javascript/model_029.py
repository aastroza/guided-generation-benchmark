# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:59:43+00:00

from __future__ import annotations

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class EventScheduler(BaseModel):
    events: Dict[str, Any] = Field(
        ...,
        description='An object mapping event names to events or arrays that define an event and its prerequisites.',
    )
    concurrencyLimit: Optional[float] = Field(
        0.0,
        description='The maximum number of events that can be scheduled concurrently. Optional parameter. Default 0.0 This is a float type value.',
    )
    callback: Optional[str] = Field(
        '',
        description='A callback function that is invoked after all events have concluded or if an error has occurred. Optional parameter. Default null',
    )
