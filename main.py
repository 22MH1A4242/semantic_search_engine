from fastapi import FastAPI
from pydantic import BaseModel

from data_loader import load_documents
from embedder import embed_texts
from faiss_index import build_index
from search import semantic_search

app = FastAPI(title="Distributed Semantic Search Engine")

documents = load_documents()
embeddings = embed_texts(documents)
index = build_index(embeddings)

class SearchRequest(BaseModel):
    query: str
    top_k: int = 3

@app.post("/search")
def search_endpoint(request: SearchRequest):
    results = semantic_search(index, documents, request.query, request.top_k)
    return {"query": request.query, "results": results}
