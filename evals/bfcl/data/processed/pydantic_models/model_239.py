# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:42:21+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class UsPresidentInYear(BaseModel):
    year: int = Field(..., description='The year in question.')
    full_name: Optional[bool] = Field(
        True,
        description='Option to return full name with middle initial, if applicable.',
    )
