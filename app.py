from fastapi import FastAPI, File, UploadFile
from utils import analyze_answer, transcribe_audio_file

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Interview Coach using Azure AI Foundry is running"}

@app.get("/interview")
def get_followup(candidate_input: str, job_role: str = "software engineer"):
    return {"response": analyze_answer(candidate_input, job_role)}

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    transcript = transcribe_audio_file(audio_bytes)
    return {"transcript": transcript}