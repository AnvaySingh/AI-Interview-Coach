import os
from openai import AzureOpenAI

client = AzureOpenAI(azure_endpoint=os.getenv("OPENAI_ENDPOINT"),
api_version="2023-03-15-preview",
api_key=os.getenv("OPENAI_API_KEY"))
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

load_dotenv()


# GPT-4 prompt and completion

def analyze_answer(candidate_input, job_role="software engineer"):
    system_prompt = f"You are an experienced recruiter interviewing for a {job_role} role."
    user_prompt = f"The candidate responded with:\n{candidate_input}\n\nNow give a follow-up question, sentiment, tone, and coaching tip."

    response = client.chat.completions.create(model=os.getenv("OPENAI_DEPLOYMENT"),
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ])
    return response.choices[0].message.content

# Azure Speech-to-Text

def transcribe_audio():
    speech_config = speechsdk.SpeechConfig(
        subscription=os.getenv("SPEECH_KEY"),
        region=os.getenv("SPEECH_REGION")
    )
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config
    )
    print("Speak now...")
    result = recognizer.recognize_once()
    return result.text