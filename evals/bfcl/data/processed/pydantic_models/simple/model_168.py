# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:55:29+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Status(Enum):
    ongoing = 'ongoing'
    settled = 'settled'
    dismissed = 'dismissed'


class LawsuitSearch(BaseModel):
    company: str = Field(..., description='The company related to the lawsuit.')
    start_date: str = Field(
        ...,
        description='Start of the date range for when the lawsuit was filed in the format of MM-DD-YYY.',
    )
    location: str = Field(
        ...,
        description='Location where the lawsuit was filed in the format of full state name.',
    )
    status: Optional[Status] = Field(
        Status.ongoing, description="The status of the lawsuit. Default is 'ongoing'."
    )
