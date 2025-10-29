# 📰 Multilingual News Summarizer (with Speech Support)

An AI-powered application that fetches news in multiple languages, summarizes the content using NLP, and provides speech output using TTS. Designed to make staying informed faster, multilingual, and more accessible.

---

## 🚀 Features

- 🌐 **Multilingual Support**  
  Fetch and summarize news in English, Hindi, Spanish, and other languages.

- 🧠 **AI-Based Summarization**  
  Uses NLP techniques to generate concise and readable summaries from full-length news articles.

- 🔊 **Speech Output**  
  Converts text summaries into natural speech using Text-to-Speech (TTS) engines.

- 📰 **Live News Fetching**  
  Integrates with NewsAPI to fetch trending news by category and language.

- 🖥️ **User-Friendly Interface**  
  Intuitive UI for language selection, category filtering, and audio playback.

---

## 🛠️ Tech Stack

| Component        | Technology                          |
|------------------|--------------------------------------|
| Backend          | Python, Flask / FastAPI              |
| NLP              | Transformers (BART/T5), NLTK, spaCy  |
| TTS              | gTTS, pyttsx3, Google Text-to-Speech |
| Frontend         | HTML, CSS, JavaScript / Streamlit    |
| APIs             | NewsAPI, Google News API             |
---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/multilingual-news-summarizer.git
cd multilingual-news-summarizer
pip install -r requirements.txt
python app.py
