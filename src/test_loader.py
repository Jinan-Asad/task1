from loader import load_and_split

chunks = load_and_split()

print(f"Number of chunks: {len(chunks)}")

for chunk in chunks[:3]:
    print("-" * 50)
    print("File:", chunk["file"])
    print(chunk["text"][:200])