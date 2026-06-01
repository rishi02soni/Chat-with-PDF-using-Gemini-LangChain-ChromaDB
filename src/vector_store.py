from langchain_community.vectorstores import Chroma


def create_vector_store(
        documents,
        embeddings
):

    db = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory="db"
    )

    return db
