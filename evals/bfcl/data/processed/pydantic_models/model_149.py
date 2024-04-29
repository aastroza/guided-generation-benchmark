# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:41:16+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class GetStockPrice(BaseModel):
    company_names: List[str] = Field(
        ..., description='The list of companies for which to retrieve the stock price.'
    )
