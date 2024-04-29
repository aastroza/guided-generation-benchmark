# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:45:03+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class RootobjectmapperDoxcontent(BaseModel):
    builder: str = Field(
        ..., description='The XContentBuilder to which the content should be written.'
    )
    params: List[str] = Field(
        ...,
        description='Parameters controlling the serialization, including whether to include defaults and whether to skip runtime fields.',
    )
