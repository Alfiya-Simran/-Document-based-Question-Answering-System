# 🧠 Document-based Question Answering System (GenAI)

This app allows users to upload documents (PDF, Word) and ask questions based on their content using GPT-4, LangChain, and vector search (ChromaDB or FAISS).

## 🔍 Features
- Upload PDF or DOCX files
- Extract & chunk text
- Embed chunks using OpenAI Embeddings
- Query-answering with context-aware GPT-4 responses
- Built with Streamlit

## 🚀 How to Run Locally

```bash
git clone https://github.com/your-username/doc-qa-app.git
cd doc-qa-app
pip install -r requirements.txt
streamlit run app.py
```

## 🧰 Tech Stack
- LangChain
- OpenAI GPT-4
- ChromaDB / FAISS
- Streamlit

## 🔑 Environment Variable
> Create a .streamlit/secrets.toml file or set environment variable
```bash
OPENAI_API_KEY = "your-api-key"
```

## 📄 Use Cases
- Legal document analysis
- Academic research Q&A
- Internal company knowledge base
