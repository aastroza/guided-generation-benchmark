# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T19:42:26+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class DiscovererGet(BaseModel):
    element_name: str = Field(..., description='The name of the element.')
    year: Optional[int] = Field(
        None,
        description='Optional parameter that refers to the year of discovery. It could be helpful in case an element was discovered more than once. Default to 0, which means not use it.',
    )
    first: Optional[bool] = Field(
        True,
        description="Optional parameter indicating if the first discoverer's name should be retrieved.",
    )
