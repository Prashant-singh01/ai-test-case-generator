import requests
import json
import re

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_test_cases(requirement: str):

    prompt = f"""
You are a senior QA engineer.

Generate test cases for the following requirement:

{requirement}

Return ONLY valid JSON in this format:

{{
 "testcases":[
   {{
     "id":"TC001",
     "title":"Short test case title",
     "type":"Positive or Negative",
     "steps":[
        "Step 1",
        "Step 2",
        "Step 3"
     ],
     "expected_result":"Expected outcome"
   }}
 ]
}}

Generate 5 test cases.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    text = result["response"]

    # Extract JSON block safely
    json_match = re.search(r"\{.*\}", text, re.DOTALL)

    if json_match:
        return json.loads(json_match.group())

    return {"error": "AI did not return valid JSON", "raw_output": text}