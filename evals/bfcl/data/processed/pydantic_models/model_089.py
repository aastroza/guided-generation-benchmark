# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:45:20+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class RunThis(BaseModel):
    argv: List[str] = Field(
        ...,
        description='An array of strings representing the command-line arguments, to include waittime and debuggeeName. Format: -waitTime, <waitTime>, -debuggeeName, TestDebuggee',
    )
    out: str = Field(..., description='The PrintStream to output the logs to.')
