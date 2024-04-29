# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:45:56+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class B(BaseModel):
    e: Optional[str] = Field(
        None,
        description='The initial task or an array of tasks to be added to the queue. Default null',
    )
    t: float = Field(
        ...,
        description='The concurrency level of the task queue. This is a float type value.',
    )
    n: Optional[float] = Field(
        None,
        description='The payload size for each task worker. Optional parameter. Default 0.0 This is a float type value.',
    )
