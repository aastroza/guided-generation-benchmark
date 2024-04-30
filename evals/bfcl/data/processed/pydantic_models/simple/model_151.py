# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:55:17+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class HighestGrossingBanks(BaseModel):
    country: str = Field(..., description='The country to get the data from.')
    year: int = Field(..., description='The year to get the data from.')
    top_n: Optional[int] = Field(
        5, description='Top n banks in terms of grossing. Default is 5'
    )
