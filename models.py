
from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class DialogueRequest(BaseModel):
    question: str
    complexity: Optional[str] = "medium"

class Claim(BaseModel):
    id: str
    text: str
    source: str
    assumptions: List[str] = []
    contradictions: List[str] = []
    fallacies: List[str] = []

class ReasoningTrace(BaseModel):
    session_id: str
    original_input: str
    processed_input: str
    claims: List[Claim] = []
    ai_prompts: List[str] = []

class DialogueResponse(BaseModel):
    response: str
    processed_input: str
    reasoning_trace: Dict[str, Any]
