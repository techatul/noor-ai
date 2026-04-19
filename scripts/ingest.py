import os
import urllib3
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Fix User-Agent warning
os.environ["USER_AGENT"] = "Noor-AI"

# Fix SSL Unverified warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ALLOWED_URLS = [
    "https://demo.kishahaldiamakeup.in",
    "https://demo.kishahaldiamakeup.in/about",
    "https://demo.kishahaldiamakeup.in/affiliate-program",
]

BLOCK_KEYWORDS = ["privacy", "terms", "login", "cart"]

def filter_urls(urls):
    filtered = []
    for url in urls:
        if any(keyword in url for keyword in BLOCK_KEYWORDS):
            continue
        filtered.append(url)
    return filtered

def run_ingestion():
    urls = filter_urls(ALLOWED_URLS)

    # Load pages
    print(f"Loading data from {len(ALLOWED_URLS)} pages...")
    loader = WebBaseLoader(
        web_paths=urls,
        verify_ssl=False
    )

    docs = loader.load()

    # Split
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(docs)

    # Embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Store in Chroma
    db = Chroma.from_documents(
        chunks,
        embedding=embeddings,
        persist_directory="data/chroma_db"
    )
    print("Success! Data saved locally...")

# Allow manual run
if __name__ == "__main__":
    run_ingestion()