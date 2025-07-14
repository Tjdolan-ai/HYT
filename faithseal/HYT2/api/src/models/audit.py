from pydantic import BaseModel
from typing import List

class AuditRequest(BaseModel):
    text: str

class AuditResponse(BaseModel):
    ethics_score: float
    concerns: List[str]
