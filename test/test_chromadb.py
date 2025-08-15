#!/usr/bin/env python3
import chromadb
from chromadb.utils import embedding_functions

def test_chromadb():
    try:
        print("Testing ChromaDB connection...")
        
        # Try to connect to the database
        client = chromadb.PersistentClient(path="./chroma_db")
        print("✅ Successfully connected to ChromaDB")
        
        # List all collections
        collections = client.list_collections()
        print(f"📚 Available collections: {[col.name for col in collections]}")
        
        # Try to get the specific collection
        try:
            sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
            collection = client.get_collection(name="support_queries", embedding_function=sentence_transformer_ef)
            print("✅ Successfully retrieved 'support_queries' collection")
            
            # Check collection info
            count = collection.count()
            print(f"📊 Collection has {count} items")
            
            # Try a simple query
            if count > 0:
                results = collection.query(query_texts=["test query"], n_results=1)
                print("✅ Successfully queried collection")
                print(f"📝 Sample metadata: {results['metadatas']}")
            else:
                print("⚠️  Collection is empty")
                
        except Exception as e:
            print(f"❌ Error getting collection: {str(e)}")
            
    except Exception as e:
        print(f"❌ Error connecting to ChromaDB: {str(e)}")

if __name__ == "__main__":
    test_chromadb() 