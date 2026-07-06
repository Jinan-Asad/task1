from loader import load_and_split
from embeddings import embed_text

chunks = load_and_split()

print("Number of chunks:", len(chunks))

# نجرب أول chunk فقط
vector = embed_text(chunks[0]["text"])

print("First embedding length:", len(vector))
print(vector[:10])