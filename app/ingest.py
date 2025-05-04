import os
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader, PyPDFLoader

# Setup paths
CHROMA_DIR = "chroma_db"
DOC_PATH = "data/sample_doc"  # File path without extension

# Load and embed documents
def setup_vector_store():
    # Ensure the data directory exists
    os.makedirs("data", exist_ok=True)

    # Load documents based on file extension
    if os.path.exists(f"{DOC_PATH}.txt"):
        loader = TextLoader(f"{DOC_PATH}.txt")
    elif os.path.exists(f"{DOC_PATH}.pdf"):
        loader = PyPDFLoader(f"{DOC_PATH}.pdf")
    else:
        raise FileNotFoundError("No supported document found. Please add a .txt or .pdf file in the data folder.")

    documents = loader.load()
    print(f"Loaded {len(documents)} documents from {DOC_PATH}.")  # Debug statement

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    split_docs = splitter.split_documents(documents)
    print(f"Split into {len(split_docs)} document chunks.")  # Debug statement

    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")  # Explicitly specify model_name
    vectordb = Chroma.from_documents(split_docs, embedding_model, persist_directory=CHROMA_DIR)
    # Removed vectordb.persist() as persistence is now automatic
    print("Vector store created and persisted.")  # Debug statement
    return vectordb

# Search using similarity
vectordb = setup_vector_store()

def search_context(query: str):
    docs = vectordb.similarity_search(query, k=3)
    print(f"Query: {query}")  # Debug statement
    print(f"Retrieved {len(docs)} documents.")  # Debug statement
    for i, doc in enumerate(docs):
        print(f"Document {i+1}: {doc.page_content}")  # Debug: Print retrieved chunks
    return "\n".join([doc.page_content for doc in docs])
