
# 🎤 AI Interview Coach

A smart, voice-enabled interview coach powered by **Azure OpenAI (GPT-4)** and **Azure Speech Services**. It listens to your answer (via voice or text), provides feedback, and asks insightful follow-up questions — just like a real recruiter!

---

## 🚀 Features

- ✅ GPT-4 analysis & coaching  
- ✅ Follow-up question generation  
- ✅ Voice-to-text via Azure Speech  
- ✅ FastAPI backend + Streamlit frontend  
- ✅ No personal data stored  

---

## 📁 Project Structure

```
ai-interview-coach/
├── app.py                  # FastAPI backend
├── interview_ui.py         # Streamlit frontend (voice-enabled)
├── utils.py                # GPT + Speech helper functions
├── prompt_templates/       # Prompt templates
│   └── interview_followup.txt
├── .env                    # 🔒 DO NOT COMMIT (contains API keys)
├── .env.example            # ✅ Shareable env template
├── requirements.txt        # Python dependencies
└── README.md               # You're here
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/ai-interview-coach.git
cd ai-interview-coach
```

### 2. Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate    # Windows: .\env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example file and update it with your credentials:

```bash
cp .env.example .env
```

Edit `.env` with:

```
OPENAI_API_KEY=your-azure-openai-key
OPENAI_ENDPOINT=https://your-openai-resource.openai.azure.com/
OPENAI_DEPLOYMENT=gpt-4

SPEECH_KEY=your-azure-speech-key
SPEECH_REGION=your-region
```

---

## ▶️ How to Run

### 1. Start Backend API

```bash
uvicorn app:app --reload
```

Swagger UI: http://localhost:8000/docs

### 2. Start the Streamlit App

Open a **new terminal** and run:

```bash
streamlit run interview_ui.py
```

---

## 🧠 How It Works

1. Choose text or voice to answer.
2. Transcribes voice input using Azure Speech.
3. Sends input to GPT-4 via Azure OpenAI.
4. Returns:
   - A follow-up question  
   - Sentiment & tone analysis  
   - Coaching tips  

---

## 💡 Tech Stack

- **Azure OpenAI** (GPT-4)
- **Azure Speech Services**
- **FastAPI**
- **Streamlit**
- **Python 3.9+**

---

## 🔄 Future Enhancements

- Upload & parse resumes for custom coaching  
- Real-time feedback with WebSockets  
- Save sessions to Azure CosmosDB or Blob  
- Deploy on Azure App Service  


---

## 📄 License

MIT License
