from fastapi import FastAPI
from backend.models.schemas import AnswerRequest, InterviewResponse
from backend.interview.engine import generate_next_question
from backend.interview.evaluator import evaluate_answer

app = FastAPI(title="AI Interviewer")

SESSION_MEMORY = {}

@app.post("/interview/answer", response_model=InterviewResponse)
def submit_answer(data: AnswerRequest):

    session = SESSION_MEMORY.get(data.session_id, [])
    session.append(f"Q: {data.question}\nA: {data.answer}")

    evaluation = evaluate_answer(data.question, data.answer)

    next_question = generate_next_question(session)

    SESSION_MEMORY[data.session_id] = session

    return InterviewResponse(
        next_question=next_question,
        score=evaluation.get("score", 5),
        feedback=evaluation.get("feedback", "")
    )
