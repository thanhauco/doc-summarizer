from langchain.vectorstores import FAISS
def create_index(docs):
    return FAISS.from_documents(docs)