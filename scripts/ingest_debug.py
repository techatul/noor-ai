# debug_ingest.py
from app.db.vectordb import load_vectorstore

db = load_vectorstore()

docs = db.similarity_search("test", k=3)
print(docs)
print(f"Total documents in collection: {db._collection.count()}")
# for d in docs:
#     print("SOURCE:", d.metadata.get("source"))
#     print("CONTENT:", d.page_content[:200])
#     print("-" * 50)

# print("✅ Ingestion complete!")