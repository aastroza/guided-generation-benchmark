# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:59:46+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class EmitNewLineBeforeLeadingComments(BaseModel):
    lineMap: str = Field(
        ..., description='An object representing the line map of the TypeScript file.'
    )
    writer: str = Field(
        ..., description='An object used for writing to the TypeScript file.'
    )
    node: int = Field(..., description='The position of the node..')
    leadingComments: Optional[str] = Field(
        '',
        description='An array of leading comment objects associated with the node. Default empty array',
    )
