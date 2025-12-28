import requests

BACKEND_URL = "http://127.0.0.1:8000"

def submit_answer(session_id, question, answer):
    payload = {
        "session_id": session_id,
        "question": question,
        "answer": answer
    }

    response = requests.post(
        f"{BACKEND_URL}/interview/answer",
        json=payload
    )

    return response.json()
