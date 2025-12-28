import json
from backend.llm.client import call_llm
from backend.llm.prompts import EVALUATION_PROMPT

def evaluate_answer(question, answer):
    messages = [
        {"role": "system", "content": EVALUATION_PROMPT},
        {
            "role": "user",
            "content": f"Question: {question}\nAnswer: {answer}"
        }
    ]

    response = call_llm(messages)
    try:
        return json.loads(response)
    except:
        return {
            "score": 5,
            "strengths": "Average understanding",
            "weaknesses": "Needs improvement",
            "feedback": response
        }
