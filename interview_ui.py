import streamlit as st
import requests
from st_audiorec import st_audiorec  # <-- Add this import

# API_BASE = "https://aiinterviewcoach-api.azurewebsites.net"
API_BASE = "http://localhost:8000"

st.title("🎤 AI Interview Coach")
st.markdown("Answer an interview question and get feedback + a follow-up question.")

use_voice = st.checkbox("🎙️ Use my voice to answer")
input_text = ""
job = st.selectbox("💼 Choose a Job Role:", ["software engineer", "product manager", "data analyst"])

if use_voice:
    st.info("Click 'Start Recording', answer, then click 'Stop'.")
    audio_bytes = st_audiorec()
    if audio_bytes is not None:
        st.audio(audio_bytes, format="audio/wav")
        if st.button("Transcribe My Answer"):
            with st.spinner("Transcribing..."):
                files = {"file": ("audio.wav", audio_bytes, "audio/wav")}
                try:
                    response = requests.post(f"{API_BASE}/transcribe", files=files)
                    if response.status_code == 200:
                        input_text = response.json()["transcript"]
                        st.session_state["input_text"] = input_text
                        st.text_area("🎤 Transcribed Answer:", value=input_text, height=150, key="voice_input")
                    else:
                        st.error("Transcription error.")
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
