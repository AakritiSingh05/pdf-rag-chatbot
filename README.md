# 📄 PDF RAG Chatbot (Local AI)

An AI-powered chatbot that can answer questions from PDF documents using Retrieval-Augmented Generation (RAG).  
This project runs completely **locally**, ensuring **zero API cost** and **full data privacy**.

---

## 🚀 Problem Statement

Reading large PDFs (notes, books, reports) is time-consuming, especially when searching for specific information.  
Users often waste time scrolling and manually finding answers.

---

## 💡 Solution

This chatbot allows users to:
- Upload PDF documents
- Ask questions in natural language
- Get accurate, context-aware answers instantly

It uses **RAG (Retrieval-Augmented Generation)** to fetch relevant content from PDFs and generate responses using a local LLM.

---

## 🔥 Key Features

- 📂 Upload and process PDF files
- 💬 Ask questions based on document content
- ⚡ Fast and relevant answers using vector search
- 🔒 100% local execution (no external API calls)
- 💰 Zero cost (uses Ollama locally)
- 🧠 Context-aware responses using embeddings

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (Frontend UI)
- **LangChain** (RAG pipeline)
- **FAISS** (Vector database)
- **Ollama** (Local LLM)
- **PyPDF** (PDF processing)

---

## 🧠 How It Works

1. PDF is loaded and split into smaller chunks  
2. Each chunk is converted into embeddings  
3. Embeddings are stored in FAISS vector database  
4. User asks a question  
5. Relevant chunks are retrieved  
6. Local LLM (via Ollama) generates the final answer  

---

### Installation and Setup

'''bash
# Clone the repository
git clone https://github.com/AakritiSingh05/pdf-rag-chatbot.git
cd pdf-rag-chatbot

# Create virtual environment
python3 -m venv venv

# Activate environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start Ollama
ollama serve

# Pull model (run once)
ollama pull llama3

# Run application
streamlit run src/app.py

### Project Structure

pdf-rag-chatbot/
│── src/
│   ├── app.py              # Streamlit UI
│   ├── rag_chain.py        # RAG pipeline logic
│   ├── pdf_loader.py       # PDF processing
│   ├── vector_store.py     # FAISS vector DB
│   └── config.py           # Configuration
│
│── data/                   # Processed data (optional)
│── pdfs/                   # Input PDFs
│── requirements.txt        # Dependencies

## Usage

1. Start the application  
2. Upload a PDF file  
3. Ask questions in the chat interface  
4. Get answers based on the uploaded document  

The system retrieves relevant content and generates accurate responses using a local LLM.

## Highlights

- Runs completely locally using Ollama  
- No external API calls  
- Ensures full data privacy  
- Zero operational cost  

## Future Improvements

- Support for multiple PDF uploads  
- Add chat history memory  
- Improve UI/UX of chatbot  
- Add support for image-based PDFs (OCR)  
- Deploy on cloud for public access

  



