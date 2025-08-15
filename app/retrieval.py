import chromadb
import os
from chromadb.utils import embedding_functions

def get_collection():
    # Get the absolute path to the chroma_db directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    chroma_path = os.path.join(project_root, "chroma_db")
    
    client = chromadb.PersistentClient(path=chroma_path)
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    return client.get_collection(name="support_queries", embedding_function=sentence_transformer_ef)

def retrieve_similar(query, k=3):
    collection = get_collection()
    results = collection.query(query_texts=[query], n_results=k)
    return results['metadatas'][0]  # List of dicts with 'query' and 'response'