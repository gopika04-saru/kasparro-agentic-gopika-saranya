from pydantic import BaseModel
from typing import List

class AgentOutput(BaseModel):
    status: str
    execution_steps: List[str]
    final_result: str
