from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from data_loader import load_corpus_from_json
from faiss_index import save_index
from tqdm import tqdm

def build_faiss_index(corpus):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = []

    print("🔢 Generating embeddings...")
    for text in tqdm(corpus):
        emb = model.encode(text)
        embeddings.append(emb)

    embeddings = np.array(embeddings).astype("float32")

    print("📦 Building FAISS index...")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    id_mapping = list(range(len(corpus)))  # Ensure mapping is integer-based

    return index, id_mapping

def main():
    corpus, _ = load_corpus_from_json("News_Category_Dataset_v3.json")
    index, id_mapping = build_faiss_index(corpus)
    print("💾 Saving index and ID mapping...")
    save_index(index, id_mapping)
    print("✅ Index built and saved from JSON dataset.")

if __name__ == "__main__":
    main()
