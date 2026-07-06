# CineMatch 🎬

A semantic movie recommendation system that understands what you're looking for in natural language. Describe the kind of film you want to watch and CineMatch finds the five most relevant matches from the database — capturing meaning and context rather than relying on keyword matching alone.

---

## How It Works

1. The publicly available Kaggle Movies Dataset is loaded and preprocessed
2. Movie metadata is chunked and embedded into a ChromaDB vector store using OpenAI embeddings
3. The user describes the type of movie they want to watch in plain natural language
4. The query is converted to a vector embedding and semantically matched against the database
5. The five most relevant movies are returned based on contextual similarity

---

## Example

```
Query: "sci-fi superhero film with plenty of action"

Results:
1. Megamind
2. Batman v Superman: Dawn of Justice
3. Avengers: Age of Ultron
4. ...
```

---

## Project Structure

```
├── data/                  # Kaggle Movies Dataset
├── chroma/                # ChromaDB vector store (auto-generated)
├── createdb.py            # Ingests and embeds movie data into ChromaDB
├── query.py               # Interactive recommendation interface
├── .env                   # API key (not committed)
├── .gitignore
└── requirements.txt
```

---

## Setup

**1. Clone the repository and create a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your OpenAI API key to `.env`**
```
OPENAI_API_KEY=your-key-here
```

**4. Build the vector store**
```bash
python ingest.py
```

**5. Run CineMatch**
```bash
python search.py
```

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| LangChain | Document loading, chunking, prompt orchestration |
| ChromaDB | Vector store and similarity search |
| OpenAI Embeddings | Query and document vectorisation |
| Kaggle Movies Dataset | Movie metadata source |
| python-dotenv | API key management |

---

## Dataset

The [Kaggle Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) is a publicly available collection of metadata for over 45,000 movies, including titles, genres, overviews, release dates, and more. CineMatch uses this metadata as the knowledge base for semantic search.
