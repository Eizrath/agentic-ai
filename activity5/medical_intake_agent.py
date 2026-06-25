import os
import json
from enum import Enum
from pydantic import BaseModel, Field, ValidationError
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

class Severity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class Symptom(BaseModel):
    symptom_name: str
    severity: Severity
    duration_days: int = Field(ge=0)

class MedicalIntake(BaseModel):
    symptoms: list[Symptom]
    allergies: list[str]
    urgency_rating: int = Field(ge=1, le=10)
    clinical_reasoning: str

def process_intake(patient_input: str) -> MedicalIntake:
    max_retries = 3

    system_prompt = (
        "You are a clinical intake assistant. Extract structured medical information from the patient's description. "
        "urgency_rating must be an integer between 1 and 10 (inclusive). "
        "duration_days must be 0 or greater. "
        "severity must be one of: LOW, MEDIUM, HIGH. "
        "Respond only with valid JSON matching the required schema."
    )

    contents = [
        {"role": "user", "content": patient_input}
    ]

    for attempt in range(1, max_retries + 1):
        print(f"\n[Attempt {attempt}]")

        messages = [types.Content(role=c["role"], parts=[types.Part(text=c["content"])]) for c in contents]

        # On the first attempt, omit response_schema so the model returns the
        # raw value from the user input (e.g. urgency 15), triggering ValidationError.
        # On retries, enforce the schema so constrained decoding keeps it valid.
        if attempt == 1:
            config = types.GenerateContentConfig(
                system_instruction=system_prompt,
                response_mime_type="application/json",
            )
        else:
            config = types.GenerateContentConfig(
                system_instruction=system_prompt,
                response_mime_type="application/json",
                response_schema=MedicalIntake,
            )

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=messages,
            config=config,
        )

        raw = response.text
        print(f"[Raw Response]: {raw}")

        try:
            data = json.loads(raw)
            record = MedicalIntake(**data)
            print("[Validation Passed]")
            return record
        except ValidationError as e:
            print(f"[ValidationError on attempt {attempt}]:\n{e}")
            if attempt == max_retries:
                raise Exception(f"Failed after {max_retries} attempts. Last error: {e}")

            # Append assistant response and error feedback to history
            contents.append({"role": "model", "content": raw})
            contents.append({
                "role": "user",
                "content": (
                    f"Your previous response failed validation with the following error:\n{e}\n\n"
                    "Please fix the issues and return a corrected valid JSON response."
                )
            })

if __name__ == "__main__":
    test_input = "My stomach is cramping incredibly badly since last night! The pain is unbearable, definitely an urgency of 15 out of 10! I don't think I have allergies."
    try:
        record = process_intake(test_input)
        print("\n--- Validated Intake Record ---")
        print(record.model_dump_json(indent=2))
    except Exception as e:
        print(f"Failed: {e}")