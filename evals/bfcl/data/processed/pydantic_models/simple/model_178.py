# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:55:36+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class AdditionalDetail(Enum):
    attorneys = 'attorneys'
    plaintiffs = 'plaintiffs'
    defendants = 'defendants'
    charges = 'charges'
    court_updates = 'court_updates'


class GetLawsuitDetails(BaseModel):
    case_number: str = Field(..., description='The case number of the lawsuit.')
    court_location: str = Field(
        ..., description='The location of the court where the case is filed.'
    )
    additional_details: Optional[List[AdditionalDetail]] = Field(
        [AdditionalDetail.attorneys, AdditionalDetail.plaintiffs, AdditionalDetail.defendants, AdditionalDetail.charges, AdditionalDetail.court_updates],
        description='Optional. Array containing additional details to be fetched. Default is all.',
    )
