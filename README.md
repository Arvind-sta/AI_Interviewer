# 🧠 AI Interviewer – LLM Powered Interview Platform

## 📌 Overview
AI Interviewer is a job-ready AI system that conducts adaptive technical interviews using Large Language Models (LLMs).  
It dynamically asks questions, evaluates candidate responses, provides structured feedback, and assigns performance scores in real time.

This project demonstrates real-world AI Engineering skills including backend API development, LLM integration, session management, and frontend interaction.

---

## 🚀 Key Features
- Adaptive interview questions with increasing difficulty
- Automated answer evaluation with scoring (0–10)
- Instant feedback after each response
- Session-based interview flow
- Clean backend architecture using FastAPI
- Interactive frontend built with Streamlit
- Secure environment variable handling
- Production-ready and scalable structure

---

## 🏗️ System Architecture
User (Browser)
↓
Streamlit Frontend
↓
FastAPI Backend
↓
LLM (OpenAI)
↓
Evaluation & Scoring Engine


---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- OpenAI API
- Pydantic
- Uvicorn

### Frontend
- Streamlit
- Requests

### Tools & DevOps
- Git & GitHub
- Virtual Environment (venv)

---

## 📂 Project Structure
AI_INTERVIEWER/
├── backend/
│ ├── main.py
│ ├── config.py
│ ├── interview/
│ │ ├── engine.py
│ │ └── evaluator.py
│ ├── llm/
│ │ ├── client.py
│ │ └── prompts.py
│ └── models/
│ └── schemas.py
│
├── frontend/
│ ├── app.py
│ └── api.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md

---

## ⚙️ Installation & Setup

### Clone Repository
```bash
git clone https://github.com/Arvind-sta/AI_Interviewer.git
cd AI_Interviewer

###create the environment and activate it 
python -m venv venv
venv\Scripts\activate

###install the all requairement 
pip install -r requirements.txt

###Create a .env file in the project root:
OPENAI_API_KEY=your_openai_api_key_here

###start backend
uvicorn backend.main:app --reload

### start frontend 
streamlit run frontend/app.py

than use it for interview 

