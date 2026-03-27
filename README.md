🦙 Llama Document RAG Assistant - Insight RAG

A lightweight Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask natural language questions using LLaMA 3.3 (Groq) and Chroma vector database.

🚀 Features
📄 Upload PDF documents
🔍 Automatic document chunking and embedding
🧠 Semantic search using HuggingFace embeddings
💬 Ask questions in natural language
⚡ Fast inference using Groq-hosted LLaMA 3.3 (70B)
🗂 Persistent vector storage with ChromaDB


🏗️ Tech Stack
LLM: LLaMA 3.3 (Groq API)
Embeddings: HuggingFace Sentence Transformers
Vector DB: ChromaDB
Framework: LangChain
Frontend: Streamlit
Document Loader: UnstructuredFileLoader


📁 Project Structure
QA_RAG_Dynamicpdf/
│
├── QA_app.py                  # Streamlit UI
├── rag_utility.py          # RAG pipeline logic
└── requirements.txt


⚙️ Setup Instructions
1. Clone the repository
```
git clone https://github.com/saamm/QA_RAG_Dynamicpdf
```

```
cd QA_RAG_Dynamicpdf
```
2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Set environment variables
Create a .env file:
```
GROQ_API_KEY=your_api_key_here
```
5. Run the app
```
streamlit run QA_app.py
```

🧠 How It Works
Upload a PDF document
Document is split into chunks
Chunks are embedded using HuggingFace embeddings
Stored in Chroma vector database
User queries are converted into embeddings
Relevant chunks are retrieved and passed to LLaMA 3.3 for answering


📌 Notes
Vector database is persisted locally in doc_vectorstore/
First run may take time due to embedding model loading
Designed for single-document Q&A use cases
