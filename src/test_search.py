from search import search

results = search("How many annual leave days do employees have?")

for r in results:
    print("=" * 50)
    print(r["file"])
    print(r["text"])