# 💬 Bedrock Knowledge Base + Gemini 2.5 Flash Chatbot

A **Retrieval-Augmented Generation (RAG)** application that integrates Amazon Bedrock Knowledge Base with Google Gemini 2.5 Flash to provide accurate, context-aware responses.

---

## 🚀 Overview

This project demonstrates a scalable GenAI architecture that combines **semantic retrieval** with **large language models** to deliver reliable answers grounded in enterprise data.

---

## 🧠 Architecture

1. User submits a query through the Streamlit interface
2. Query is sent to Amazon Bedrock Knowledge Base
3. Relevant document chunks are retrieved
4. Context is passed to Gemini 2.5 Flash
5. The model generates a response based on retrieved data
6. The answer and supporting context are displayed

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Retrieval:** Amazon Bedrock Knowledge Base
* **LLM:** Gemini 2.5 Flash
* **SDK:** Boto3
* **Configuration:** python-dotenv

---

## 📂 Project Structure

```
kb-gemini-chat/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│── .env.example
```

---

## ⚙️ Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/kb-gemini-chat.git
cd kb-gemini-chat
```

### 2. Create a virtual environment

```
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```
AWS_REGION=your_region
KNOWLEDGE_BASE_ID=your_kb_id
GEMINI_API_KEY=your_api_key
```

### 5. Run the application

```
streamlit run app.py
```

---

## 🔐 Security

* Sensitive credentials are managed via environment variables
* `.env` is excluded from version control using `.gitignore`
* No secrets are stored in the codebase

---

## 💡 Features

* Semantic search using Bedrock Knowledge Base
* Context-aware answer generation with Gemini
* Reduced hallucination through controlled prompting
* Interactive UI with Streamlit
* Optional visibility of retrieved context

---

## 📜 License

This project is licensed under the MIT License.
