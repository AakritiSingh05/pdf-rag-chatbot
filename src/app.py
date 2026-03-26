import streamlit as st
from pdf_loader import load_and_split
from vector_store import create_vector_store
from rag_chain import get_answer

st.title("📄 PDF Chatbot")

if st.button("Process PDFs"):
    docs = load_and_split()
    create_vector_store(docs)
    st.success("PDFs processed!")

query = st.text_input("Ask a question")

if query:
    answer = get_answer(query)
    st.write(answer)