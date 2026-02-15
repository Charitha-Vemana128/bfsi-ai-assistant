# BFSI AI Assistant

An AI-powered assistant designed to answer Banking, Financial Services, and Insurance (BFSI) customer queries using a multi-layer architecture.

---

## 🚀 Features

- Dataset-first response system for compliance and accuracy
- Semantic similarity search using Sentence Transformers
- RAG (Retrieval Augmented Generation) for financial knowledge queries
- Local Small Language Model fallback (TinyLlama)
- Security guardrails to block sensitive requests
- Runs completely offline on local machine

---

## 🧠 Architecture

User Query → Dataset Similarity → Knowledge Retrieval → Local LLM → Final Response

---

## 📂 Project Structure

```
app.py
dataset.json
knowledge.txt
README.md
```

---

## ⚙️ Tech Stack

- Python
- Sentence Transformers
- HuggingFace Transformers
- TinyLlama LLM
- Torch

---

## ▶️ How to Run

Install dependencies:

```
pip install sentence-transformers transformers torch
```

Run assistant:

```
python app.py
```

---

## 🛡 Safety Features

The assistant automatically blocks sensitive requests such as:

- passwords
- OTP
- CVV
- PIN
- confidential banking data

---

## 📊 Example Queries

Try asking:

- What is EMI?
- Explain repo rate
- How to check loan status?

---

## 🎯 Project Goal

This project demonstrates how BFSI customer support systems can be built using safe, efficient, and compliant AI architecture.

---

## 👤 Author

Charitha Vemana
