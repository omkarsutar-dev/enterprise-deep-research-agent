from pydantic import BaseModel
from typing import List


class CriticOutput(BaseModel):

    strengths: List[str]

    weaknesses: List[str]

    suggestions: List[str]

    score: float