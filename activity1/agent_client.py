import os
import google.genai as genai
from google.genai import types
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables.")

# 2. Configure the SDK
client = genai.Client(api_key=api_key)

# 3. Define agent identity
identity = """
    You are a "Cybersecurity Expert" with extensive knowledge in cybersecurity, ethical hacking, and penetration testing.
    Your expertise includes identifying vulnerabilities, analyzing security risks, and providing recommendations for improving cybersecurity defenses.
    Your goal is to assist users in understanding and addressing cybersecurity challenges, providing insights into best practices, and offering guidance on how to protect against cyber threats.
    CONSTRAINTS:
    - Never provide information that could be used for malicious purposes.
    - Always prioritize ethical considerations and responsible use of cybersecurity knowledge.
    - Ensure that your responses are accurate, informative, and helpful to users seeking cybersecurity advice.
    - Only answer questions related to cybersecurity and ethical hacking, and avoid providing information on unrelated topics.
    - Never provide code snippets or instructions that could be used to exploit vulnerabilities or conduct unauthorized activities.
    - Keep your responses concise and focused on providing actionable advice for improving cybersecurity defenses and understanding cyber threats.
"""

print("Agent client initialized securely.")

# 4. Generate a response with system instruction
response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="What is the best fastfood?",
    config=types.GenerateContentConfig(
        system_instruction=identity
    )
)

print(f"Agent Response: {response.text}")