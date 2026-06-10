import chromadb
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
embeddings = OpenAIEmbeddings(model=os.getenv("EMBEDDING_MODEL"))
client = chromadb.PersistentClient(path=os.getenv("CHROMA_PERSIST_DIR"))
collection = client.get_or_create_collection("schema")

def retrieve_relevant_schema(question: str, k: int = 3) -> str:
    query_vec = embeddings.embed_query(question)
    results = collection.query(query_embeddings=[query_vec], n_results=k)
    return "\n".join(results["documents"][0])