from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from config import DATA_DIR, EMBEDDING_MODEL

def create_vector_store(docs):
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(DATA_DIR)