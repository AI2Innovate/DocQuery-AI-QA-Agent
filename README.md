# DocQuery: AI QA Agent that Answers Your Uploaded PDFs and Documents with LLM + RAG

This project is an AI-powered Agent that uses a Large Language Model (LLM) and Retrieval-Augmented Generation (RAG) to answer your questions based on uploaded documents. It is designed to provide accurate and context-aware responses by leveraging the content of the documents provided by the user. The application is containerized with Docker for easy deployment.

## 🔧 Tech Stack
- Python, Streamlit
- LangChain, HuggingFace Transformers
- ChromaDB (stubbed)
- Docker

## 🚀 How to Run
```bash
git clone <this-repo>
cd llm-rag-faq-bot
pip install -r requirements.txt
uvicorn app.main:app --reload
# Then in a new terminal
streamlit run ui/streamlit_app.py
```

## 🐳 Docker
```bash
docker build -t llm-rag-faq .
docker run -p 8000:8000 llm-rag-faq
```

## 💬 Ask Questions
Use the Streamlit UI to upload documents and ask questions. The bot will analyze the uploaded documents and provide answers based on their content.
