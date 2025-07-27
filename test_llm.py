import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.responses.create(
        model="gpt-3.5-turbo",
        input = "Write a one-sentence bedtime story about a unicorn."
    )
    print(response.output_text)
except Exception as e:
    print(f"Error connecting to LLM: {e}")

