from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from config import DATA_DIR, LLM_MODEL

def get_answer(query):
    embeddings = OllamaEmbeddings(model=LLM_MODEL)
    db = FAISS.load_local(DATA_DIR, embeddings, allow_dangerous_deserialization=True)

    docs = db.similarity_search(query, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    llm = OllamaLLM(model=LLM_MODEL)

    prompt = f"""
    Answer the question using only the context below:

    {context}

    Question: {query}
    """

    return llm.invoke(prompt)