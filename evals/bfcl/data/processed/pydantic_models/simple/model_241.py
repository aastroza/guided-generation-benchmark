# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:21+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class USPresidentDuringEvent(BaseModel):
    event: str = Field(..., description='The historical event.')
    country: Optional[str] = Field(
        'USA',
        description="The country the president leads (optional parameter, defaults to 'USA' if not specified).",
    )
