
# 🎤 AI Interview Coach 

This is a smart, voice-enabled interview coach powered by **Azure OpenAI (GPT-4)** and **Azure Speech Services**.

It listens to your answer (voice or text), gives detailed feedback, and even asks you a follow-up question — like a real recruiter!

---

## 🚀 Features

✅ GPT-4 analysis & coaching  
✅ Follow-up question generation  
✅ Voice-to-text with Azure Speech  
✅ FastAPI backend + Streamlit frontend  
✅ No personal data stored  

---

## 📁 Project Structure

\`\`\`
ai-interview-coach/
├── app.py                  # FastAPI backend
├── interview_ui.py         # Streamlit frontend (voice-enabled)
├── utils.py                # GPT + Speech helper functions
├── prompt_templates/       # Prompt template(s)
│   └── interview_followup.txt
├── .env                    # 🔒 DO NOT COMMIT (holds API keys)
├── .env.example            # ✅ Use this to set up your own .env
├── requirements.txt        # Dependencies
└── README.md               # You're here
\`\`\`

---

## 🧪 How It Works

1. Choose voice or text input  
2. App records/transcribes your answer using Azure Speech  
3. Sends it to Azure OpenAI (GPT-4)  
4. Displays:
   - Follow-up question  
   - Sentiment and tone  
   - Coaching tip  

---

## ⚙️ Setup Instructions

### 1. Clone the repo

\`\`\`bash
git clone https://github.com/YOUR_USERNAME/ai-interview-coach.git

cd ai-interview-coach
\`\`\`

### 2. Create a virtual environment

\`\`\`bash
python -m venv env

source env/bin/activate  # or .\env\Scripts\activate (Windows)
\`\`\`

### 3. Install dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Set up your .env file

\`\`\`bash
cp .env.example .env
\`\`\`

Add your real Azure OpenAI & Speech keys inside `.env`.

---

## ▶️ How to Run

### Start backend API
\`\`\`bash
uvicorn app:app --reload
\`\`\`

### Start frontend UI
\`\`\`bash
streamlit run interview_ui.py
\`\`\`

---

## 🧠 Built With

- Azure OpenAI Service
- Azure Speech Services
- FastAPI
- Streamlit
- Python 3.9+

---

## 📄 License

MIT License
