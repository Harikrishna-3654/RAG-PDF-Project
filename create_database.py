from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "faiss_db",
    embeddings,
    allow_dangerous_deserialization=True
)

query = input("Ask a Question: ")

results = db.similarity_search(
    query,
    k=5
)

for i, doc in enumerate(results, 1):
    print(f"\nResult {i}")
    print(doc.page_content)