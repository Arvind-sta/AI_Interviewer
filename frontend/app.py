import streamlit as st
import uuid
from api import submit_answer

st.set_page_config(page_title="AI Interviewer")

st.title("AI Interviewer")

# create session
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
    st.session_state.question = "Tell me about yourself."

st.write("### Question")
st.write(st.session_state.question)

answer = st.text_area("Your Answer")

if st.button("Submit"):
    if answer.strip() == "":
        st.warning("Please write something.")
    else:
        result = submit_answer(
            st.session_state.session_id,
            st.session_state.question,
            answer
        )

        st.success(f"Score: {result['score']}/10")
        st.write("Feedback:")
        st.write(result["feedback"])

        st.session_state.question = result["next_question"]
        st.rerun()
