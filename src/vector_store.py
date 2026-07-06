import faiss
import numpy as np

from loader import load_and_split
from embeddings import embed_text


def build_vector_store():
    chunks = load_and_split()

    vectors = []

    for chunk in chunks:
        vector = embed_text(chunk["text"])
        vectors.append(vector)

    vectors = np.array(vectors, dtype="float32")

    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)

    return index, chunks