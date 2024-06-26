# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:56+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class RunTwoSampleTtest(BaseModel):
    group1: List[int] = Field(..., description='First group of data points.')
    group2: List[int] = Field(..., description='Second group of data points.')
    equal_variance: Optional[bool] = Field(
        True,
        description='Assumption about whether the two samples have equal variance.',
    )
