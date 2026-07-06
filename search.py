import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.PersistentClient(path="./db")
collection = client.get_or_create_collection(name="movies")

def search(query, n=5):
    embedding = model.encode(query).tolist()
    results = collection.query(query_embeddings=[embedding], n_results=n)
    for i, (doc, meta, dist) in enumerate(zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    )):
        score = round((1 - dist) * 100, 1)
        print(f"\n{i+1}. {meta['title']}  ({score}% match)")
        print(f"   {doc[:120]}...")       

while True:
    user_input = input("\nEnter a movie description to search (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    search(user_input)
