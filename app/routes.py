from fastapi import APIRouter
from app.schemas import RequirementInput
from app.ai_engine import generate_test_cases

router = APIRouter()

@router.post("/generate-testcases")
def generate(requirement: RequirementInput):
    testcases = generate_test_cases(requirement.requirement)
    return {"testcases": testcases}