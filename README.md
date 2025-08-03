# 🧑‍⚖️ AI Lawyer – Legal Question Answering with RAG & LLMs

AI Lawyer is an LLM-powered legal assistant that uses Retrieval-Augmented Generation (RAG) to answer legal questions based on context from legal documents. It leverages a vector database and a large language model (LLM) to produce accurate, context-aware responses to user queries.

---

## 🚀 Features

- 🔍 Semantic retrieval from legal documents (PDFs, text, etc.)
- 🧠 Response generation using LLMs (Groq or OpenAI)
- 📄 Handles long documents with recursive text splitting
- 🧾 Works well for use cases like contract summarization, statute lookup, legal Q&A
- 🔧 Plug-and-play architecture using LangChain, FAISS, and Groq API

---

## 🗂️ Project Structure

ai_lawyer/
├── rag_pipeline.py # Main RAG pipeline script
├── ingest.py # Script to load and index documents
├── docs/ # Folder containing legal documents (PDFs/text)
├── prompts/ # Optional prompt templates
├── requirements.txt # Python dependencies
└── README.md # Project overview

