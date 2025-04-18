from fastapi import FastAPI
from utils import analyze_answer, transcribe_audio

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Interview Coach using Azure AI Foundry is running"}

@app.get("/interview")
def get_followup(candidate_input: str, job_role: str = "software engineer"):
    return {"response": analyze_answer(candidate_input, job_role)}

@app.get("/transcribe")
def speech_to_text():
    return {"transcript": transcribe_audio()}