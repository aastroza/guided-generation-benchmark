# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:58:37+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class RedissonconnectionBitop(BaseModel):
    op: str = Field(
        ...,
        description="The BitOperation enum value representing the bitwise operation to perform. It's object represented by BitOperation.OR for or operation for example",
    )
    destination: List[str] = Field(
        ..., description='The destination key where the result will be stored.'
    )
    keys: List[str] = Field(
        ...,
        description='The source keys on which the bitwise operation will be performed.',
    )