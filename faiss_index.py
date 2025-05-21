import faiss
import pickle

def save_index(index, id_mapping, path='faiss_index'):
    faiss.write_index(index, f"{path}.index")
    with open(f"{path}_ids.pkl", "wb") as f:
        pickle.dump(id_mapping, f)

def load_faiss_index(path='faiss_index'):
    index = faiss.read_index(f"{path}.index")
    with open(f"{path}_ids.pkl", "rb") as f:
        id_mapping = pickle.load(f)
    return index, id_mapping


