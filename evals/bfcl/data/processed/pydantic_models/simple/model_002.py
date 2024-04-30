# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:53:33+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class MathHypot(BaseModel):
    x: int = Field(..., description='The x-coordinate value.')
    y: int = Field(..., description='The y-coordinate value.')
    z: Optional[int] = Field(
        0, description='Optional. The z-coordinate value. Default is 0.'
    )
