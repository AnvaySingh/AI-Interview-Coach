import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import azure.cognitiveservices.speech as speechsdk
import tempfile

# Load environment variables
load_dotenv()

# Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=os.getenv("OPENAI_ENDPOINT"),
    api_version="2023-03-15-preview",
    api_key=os.getenv("OPENAI_API_KEY")
)

# 🔍 Load external prompt template
def load_prompt_template():
    try:
        with open("prompt_templates/interview_followup.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Candidate's Role: {job_role}\nCandidate's Answer: {candidate_input}\n\nGive follow-up question and feedback."

# 🤖 GPT-4: Candidate coaching
def analyze_answer(candidate_input, job_role="software engineer"):
    prompt_template = load_prompt_template()
    full_prompt = prompt_template.format(
        job_role=job_role,
        candidate_input=candidate_input
    )

    response = client.chat.completions.create(
        model=os.getenv("OPENAI_DEPLOYMENT"),
        messages=[
            {"role": "system", "content": "You are a professional interview coach."},
            {"role": "user", "content": full_prompt}
        ]
    )

    return response.choices[0].message.content.strip()

# 🎤 Azure Speech-to-Text
def transcribe_audio():
    try:
        speech_config = speechsdk.SpeechConfig(
            subscription=os.getenv("SPEECH_KEY"),
            region=os.getenv("SPEECH_REGION")
        )
        audio_config = speechsdk.AudioConfig(use_default_microphone=True)
        recognizer = speechsdk.SpeechRecognizer(
            speech_config=speech_config,
            audio_config=audio_config
        )

        print("🎙️ Speak now...")
        result = recognizer.recognize_once()

        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return result.text
        else:
            return "Sorry, I couldn't understand you. Please try again."

    except Exception as e:
        return f"Speech recognition error: {str(e)}"

def transcribe_audio_file(audio_bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name

    try:
        speech_config = speechsdk.SpeechConfig(
            subscription=os.getenv("SPEECH_KEY"),
            region=os.getenv("SPEECH_REGION")
        )
        audio_config = speechsdk.AudioConfig(filename=tmp_path)
        recognizer = speechsdk.SpeechRecognizer(
            speech_config=speech_config,
            audio_config=audio_config
        )
        result = recognizer.recognize_once()
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return result.text
        else:
            return "Sorry, I couldn't understand the audio."
    finally:
        os.remove(tmp_path)
