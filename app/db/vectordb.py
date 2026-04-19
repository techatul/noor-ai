from sqlite3 import dbapi2
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os

_db = None
def load_vectorstore():
    global _db
    # cache_dir = "./models/all-MiniLM-L6-v2"

    if _db is not None:
        return _db

    if not os.path.exists("data/chroma_db"):
        os.makedirs("data", exist_ok=True)
        print("Chroma DB not found. Running ingestion...")
        from scripts.ingest import run_ingestion
        run_ingestion()

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    
    _db = Chroma(
        persist_directory="data/chroma_db",
        embedding_function=embeddings
    )

    return _db