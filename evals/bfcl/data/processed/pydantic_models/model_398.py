# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:44:17+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class GetMuseumHours(BaseModel):
    museum_name: str = Field(..., description='The name of the museum.')
    day: str = Field(
        ...,
        description="Day of the week. If not specified, returns the current day's hours.",
    )
