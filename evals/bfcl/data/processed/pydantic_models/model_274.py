# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:42:47+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class MuseumInfo(BaseModel):
    museum_name: str = Field(..., description='The name of the museum.')
    info_type: Optional[str] = Field(
        'opening_hours', description='The type of information needed about the museum.'
    )
