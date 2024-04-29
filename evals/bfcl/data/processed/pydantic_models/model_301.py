# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:43:06+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class GetThirdChord(BaseModel):
    key: str = Field(..., description='The key of the scale.')
    type: Optional[str] = Field(
        None,
        description="Type of the scale, either major or minor. Default is 'major'.",
    )
