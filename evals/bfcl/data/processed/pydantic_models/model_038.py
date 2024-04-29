# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:45:54+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class GetDirectoryToWatchFromFailedLookupLocationDirectory(BaseModel):
    dir: str = Field(..., description='The initial directory to consider for watching.')
    dirPath: str = Field(
        ..., description='The full path of the directory to consider for watching.'
    )
