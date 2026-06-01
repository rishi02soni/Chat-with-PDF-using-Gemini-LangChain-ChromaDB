import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
import os

# Gemini API Key
os.environ["GOOGLE_API_KEY"] = "YOUR_GEMINI_API_KEY"

st.set_page_config(page_title="PDF Chatbot")
st.title("📄 GenAI PDF Chatbot")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    loader = PyPDFLoader("temp.pdf")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = splitter.split_documents(documents)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    vectorstore = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory="./db"
    )

    retriever = vectorstore.as_retriever()

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0.2
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    st.success("PDF Processed Successfully!")

    question = st.text_input(
        "Ask a question from PDF"
    )

    if question:
        answer = qa_chain.run(question)
        st.write("### Answer")
        st.write(answer)
