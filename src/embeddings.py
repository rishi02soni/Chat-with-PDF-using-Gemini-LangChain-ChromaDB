from langchain_google_genai import GoogleGenerativeAIEmbeddings


def get_embeddings():

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    return embeddings
