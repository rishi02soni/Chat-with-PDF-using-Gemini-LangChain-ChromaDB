from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA


def create_rag_chain(retriever):

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0.3
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    return qa_chain
