import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer

df = pd.read_csv("tmdb_5000_movies.csv")[['title', 'overview']].dropna()
df=df.head(500)

model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.PersistentClient(path="./db")
collection = client.get_or_create_collection(name="movies")

print("Generating movie embeddings...")
embeddings = model.encode(df['overview'].tolist(), show_progress_bar=True)

collection.add(
    ids=[str(i) for i in df.index],
    embeddings=embeddings.tolist(),
    documents=df['overview'].tolist(),
    metadatas=[{"title": t} for t in df["title"].tolist()]
)

print("Stored", len(df), "movies in the ChromaDB collection.")
