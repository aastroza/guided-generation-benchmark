# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:15+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class MutationType(Enum):
    insertion = 'insertion'
    deletion = 'deletion'
    substitution = 'substitution'


class AnalyzeDnaSequence(BaseModel):
    sequence: str = Field(..., description='The DNA sequence to be analyzed.')
    reference_sequence: str = Field(..., description='The reference DNA sequence.')
    mutation_type: Optional[MutationType] = Field(
        MutationType.substitution,
        description="Type of the mutation to be looked for in the sequence. Default to 'substitution'.",
    )
