import streamlit as st
import requests

st.title("🎤 AI Interview Coach")

st.markdown("Answer an interview question and get feedback + a follow-up question.")

input_text = st.text_area("🗣️ Your Interview Answer:")
job = st.selectbox("💼 Choose a Job Role:", ["software engineer", "product manager", "data analyst"])

if st.button("Analyze My Answer"):
    with st.spinner("Thinking..."):
        response = requests.get("http://localhost:8000/interview", params={"candidate_input": input_text, "job_role": job})
        if response.status_code == 200:
            data = response.json()
            st.subheader("🔍 Feedback")
            st.json(data)
        else:
            st.error("Something went wrong with the backend.")