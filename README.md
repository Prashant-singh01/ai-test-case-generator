
# AI Test Case Generator

AI Test Case Generator is a backend tool that automatically generates software test cases from user requirements using an AI model.

The application accepts a functional requirement as input and produces structured test cases including test scenarios, steps, and expected results.

This project demonstrates how AI can assist QA engineers in accelerating test design and improving test coverage.

---

## Features

- Generate test cases from plain English requirements
- Covers positive and negative scenarios
- Generates structured test cases
- Includes edge cases
- REST API based architecture
- Easy to extend for automation testing frameworks

---

## Tech Stack

- Python
- FastAPI
- Ollama (Local LLM)
- Pydantic
- REST API

---

## Project Structure

```
ai-test-case-generator
│
├── app
│   ├── ai_engine.py        # AI logic for generating test cases
│   ├── routes.py           # API routes
│   ├── schemas.py          # Request/Response models
│   └── main.py             # FastAPI entry point
│
├── tests                   # Test scripts
├── requirements.txt        # Python dependencies
├── .gitignore
└── README.md
```

---

## How It Works

1. User sends a requirement to the API
2. The requirement is processed by the AI engine
3. The AI model generates structured test cases
4. The API returns the generated test cases as JSON

---

## Example Requirement

User should be able to login using email and password.

---

## Example Output

Test Case: Successful Login

Steps:
1. Open login page
2. Enter valid email
3. Enter correct password
4. Click login button

Expected Result:
User should be logged in successfully.

---

## Installation

Clone the repository

```
git clone https://github.com/yourusername/ai-test-case-generator.git
```

Navigate to the project folder

```
cd ai-test-case-generator
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Windows:

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

## Run the Application

Start the server

```
python app/main.py
```

---

## Future Improvements

- Generate automation test scripts
- Export test cases to Excel or CSV
- Add simple UI using Streamlit
- Integrate with test management tools

---

## Author

Prashant Singh
