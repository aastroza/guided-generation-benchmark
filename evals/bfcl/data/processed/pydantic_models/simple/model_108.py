# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:47+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class RunLinearRegression(BaseModel):
    predictors: List[str] = Field(
        ..., description='Array containing the names of predictor variables.'
    )
    target: str = Field(..., description='The name of target variable.')
    standardize: Optional[bool] = Field(
        False,
        description='Option to apply standardization on the predictors. Defaults to False.',
    )
