from loader import load_and_split
from embeddings import embed_text

chunks = load_and_split()

print("Creating embedding...")

vector = embed_text(chunks[0]["text"])

print("Embedding created successfully!")
print("Vector length:", len(vector))
print(vector[:10])   # أول 10 قيم فقط