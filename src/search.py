import numpy as np

from embeddings import embed_text
from vector_store import build_vector_store

# نبني قاعدة البيانات مرة واحدة
index, chunks = build_vector_store()


def search(query, top_k=3):
    # تحويل السؤال إلى Embedding
    query_vector = np.array(
        [embed_text(query)],
        dtype="float32"
    )

    # البحث عن أقرب المقاطع
    distances, indices = index.search(query_vector, top_k)

    results = []

    for i in indices[0]:
        results.append(chunks[i])

    return results