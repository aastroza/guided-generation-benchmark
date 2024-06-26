# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:59:09+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class RegexconstraintInitirpattern(BaseModel):
    category: str = Field(
        ...,
        description='The category of the constraint, which determines the pattern to be compiled.',
    )
    ruleIdx: int = Field(
        ...,
        description='The index of the rule for which the pattern is being compiled.',
    )
