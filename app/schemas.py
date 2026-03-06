from pydantic import BaseModel

class RequirementInput(BaseModel):
    requirement: str