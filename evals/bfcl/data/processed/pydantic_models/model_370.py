# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:43:56+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class SafewayOrder(BaseModel):
    location: str = Field(
        ..., description='The location of the Safeway store, e.g. Palo Alto, CA.'
    )
    items: List[str] = Field(..., description='List of items to order.')
    quantity: List[int] = Field(
        ..., description='Quantity of each item in the order list.'
    )
