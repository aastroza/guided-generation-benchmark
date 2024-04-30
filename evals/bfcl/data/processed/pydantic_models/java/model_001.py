# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:58:13+00:00

from __future__ import annotations

from typing import Any, Dict

from pydantic import BaseModel, Field


class SqlcompletionanalyzerMakeproposalsfromobject(BaseModel):
    object: str = Field(
        ..., description='The database object for which to generate proposals.'
    )
    useShortName: bool = Field(
        ..., description='Indicates whether to use short names for the proposals.'
    )
    params: Dict[str, Any] = Field(
        ..., description='A map of additional parameters to customize the proposals.'
    )