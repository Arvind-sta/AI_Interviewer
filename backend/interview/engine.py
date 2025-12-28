from backend.llm.client import call_llm
from backend.llm.prompts import INTERVIEWER_SYSTEM_PROMPT

def generate_next_question(history):
    messages = [
        {"role": "system", "content": INTERVIEWER_SYSTEM_PROMPT},
    ]

    for h in history:
        messages.append({"role": "user", "content": h})

    messages.append({
        "role": "user",
        "content": "Ask the next interview question."
    })

    return call_llm(messages)
