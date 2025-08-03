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

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Shadow-9460/ai_lawyer.git
cd ai_lawyer
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Configure Environment Variables
Create a .env file or export environment variables manually:

bash
Copy
Edit
# Example .env content
GROQ_API_KEY=your_groq_api_key_here
Alternatively, set in your terminal:

bash
Copy
Edit
export GROQ_API_KEY=your_groq_api_key_here  # Linux/macOS
set GROQ_API_KEY=your_groq_api_key_here     # Windows CMD
4. Ingest Legal Documents
Place legal documents (PDF, TXT) inside the docs/ folder, then run:

bash
Copy
Edit
python ingest.py
This script loads the files, splits the text, generates embeddings, and stores them in a vector database.

5. Run the AI Lawyer
bash
Copy
Edit
python rag_pipeline.py
When prompted, enter a legal question like:

kotlin
Copy
Edit
What are the obligations of the lessee under this lease agreement?
The system will retrieve relevant context from documents and generate a response using the LLM.

🔌 Models Supported
Groq (ultra-fast inference)

llama3-70b-8192

mixtral-8x7b-32768

OpenAI

gpt-3.5-turbo

gpt-4

Default is Groq with llama3-70b-8192, but you can swap models in rag_pipeline.py.
