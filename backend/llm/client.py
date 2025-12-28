from openai import OpenAI
from backend.config import OPENAI_API_KEY, MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)

def call_llm(messages, temperature=0.4):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content
