from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from faiss_index import load_faiss_index
from data_loader import load_corpus_from_json

model = SentenceTransformer('all-MiniLM-L6-v2')

# Load index, id mapping and corpus
index, id_mapping = load_faiss_index()
corpus, _ = load_corpus_from_json("News_Category_Dataset_v3.json")

def perform_search(query, top_k=5):
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding).astype("float32"), top_k)

    print("\n🔍 Top Results:\n")
    for i in I[0]:
        doc_id = id_mapping[i]  # should already be int
        if 0 <= doc_id < len(corpus):
            print(f"• {corpus[doc_id]}\n")

         

