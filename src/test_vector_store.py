from vector_store import build_vector_store

index, chunks = build_vector_store()

print("Vector database created successfully!")
print("Number of vectors:", index.ntotal)