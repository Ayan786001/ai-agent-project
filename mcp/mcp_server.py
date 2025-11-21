from fastapi import FastAPI

app = FastAPI()

# Dummy seed docs - normalt ville du hente dette fra Qdrant
seed_docs = [
    {"id": 1, "title": "Introduktion til RAG", "snippet": "RAG handler om retrieval + generation", "date": "2025-11-21"},
    {"id": 2, "title": "Qdrant Oversigt", "snippet": "Qdrant er en vektor database", "date": "2025-11-21"},
    {"id": 3, "title": "n8n Workflows", "snippet": "n8n bruges til at orkestrere flows", "date": "2025-11-21"},
]

@app.get("/query_knowledge_base")
def query_knowledge_base(query: str = "AI", top_k: int = 5):
    # Returner dummy data
    return {
        "query": query,
        "results": seed_docs[:top_k]
    }

@app.get("/get_recent_additions")
def get_recent_additions(days: int = 7):
    # Returner dummy data som om det er nyeste
    return {
        "days_checked": days,
        "recent_docs": seed_docs
    }
