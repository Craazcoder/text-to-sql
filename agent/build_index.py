from agent.semantic_layer import SEMANTIC_LAYER
from agent.retriever import collection, embeddings

docs, ids = [], []
for table, info in SEMANTIC_LAYER.items():
    text = f"Table: {table}. {info['description']}"
    docs.append(text)
    ids.append(table)

vecs = embeddings.embed_documents(docs)
collection.add(documents=docs, embeddings=vecs, ids=ids)
print("ChromaDB index built successfully!")