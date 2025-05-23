import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API base URL from environment variable, fallback to localhost for development
API_BASE = os.getenv("API_BASE_URL", "http://localhost:8000")

st.title("🎤 AI Interview Coach")
st.markdown("Answer an interview question and get feedback + a follow-up question.")

use_voice = st.checkbox("🎙️ Use my voice to answer")
input_text = ""
job = st.selectbox("💼 Choose a Job Role:", ["software engineer", "product manager", "data analyst"])

if use_voice:
    if st.button("🎧 Record My Answer"):
        with st.spinner("Listening and transcribing..."):
            try:
                response = requests.get(f"{API_BASE}/transcribe")
                if response.status_code == 200:
                    input_text = response.json()["transcript"]
                    st.session_state["input_text"] = input_text
                    st.text_area("🎤 Transcribed Answer:", value=input_text, height=150, key="voice_input")
                else:
                    st.error("Microphone or transcription error.")
            except Exception as e:
                st.error(f"Error calling backend: {e}")
else:
    input_text = st.text_area("🗣️ Your Interview Answer:", key="text_input")
    st.session_state["input_text"] = input_text

if st.button("Analyze My Answer") and st.session_state.get("input_text"):
    with st.spinner("Thinking..."):
        try:
            response = requests.get(f"{API_BASE}/interview", params={
                "candidate_input": st.session_state["input_text"],
                "job_role": job
            })
            if response.status_code == 200:
                data = response.json()
                st.subheader("🔍 Feedback")
                st.write(data["response"])
            else:
                st.error("Something went wrong with the backend.")
        except Exception as e:
            st.error(f"Error contacting backend: {e}")
