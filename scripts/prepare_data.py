import pandas as pd
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions
import os

# Load dataset
print("Loading dataset...")
df = pd.read_csv('data/raw/twcs.csv')
print(f"Loaded {len(df)} total rows")

# To speed up, sample 10000 rows (full dataset is large)
df = df.sample(10000, random_state=42)
print(f"Sampled {len(df)} rows")

# Extract support tweets (outbound from companies)
support_tweets = df[~df['inbound']].copy()
print(f"Found {len(support_tweets)} support tweets")

# Handle in_response_to_tweet_id - convert to int first to remove .0, then to string
support_tweets['query_id'] = support_tweets['in_response_to_tweet_id'].fillna(0).astype(int).astype(str)
df['tweet_id'] = df['tweet_id'].astype(str)

print(f"Sample query_ids: {support_tweets['query_id'].head(5).tolist()}")
print(f"Sample tweet_ids: {df['tweet_id'].head(5).tolist()}")

# Merge to get query text - this gets the original customer query
queries = df[['tweet_id', 'text']].rename(columns={'tweet_id': 'query_id', 'text': 'query_text'})
pairs = support_tweets.merge(queries, on='query_id', how='left')
print(f"After merge: {len(pairs)} pairs")

# Filter for AppleSupport (as example company) and drop missing queries
pairs = pairs[pairs['author_id'] == 'AppleSupport']
print(f"After AppleSupport filter: {len(pairs)} pairs")

# Drop rows where query_id is empty (these are not responses to customer queries)
pairs = pairs[pairs['query_id'] != '0']
print(f"After dropping empty query_id: {len(pairs)} pairs")

pairs = pairs.dropna(subset=['query_text'])
print(f"After dropping NaN queries: {len(pairs)} pairs")

# Check if we have any data left
if len(pairs) == 0:
    print("ERROR: No data left after filtering! Let's check what companies are available...")
    print("Available companies:", df['author_id'].unique())
    print("Available inbound values:", df['inbound'].unique())
    exit(1)

# Take a small corpus (1000 pairs) for demo
pairs = pairs.head(1000)
print(f"Final dataset size: {len(pairs)} pairs")

# Show sample data
print("\nSample data:")
print(pairs[['author_id', 'query_text', 'text']].head())

# Embed queries
print("\nLoading sentence transformer model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

# Set up ChromaDB
print("Setting up ChromaDB...")
client = chromadb.PersistentClient(path="./chroma_db")
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
collection = client.get_or_create_collection(name="support_queries", embedding_function=sentence_transformer_ef)

# Prepare data for addition
ids = [str(i) for i in range(len(pairs))]
queries_list = pairs['query_text'].tolist()
print(f"Encoding {len(queries_list)} queries...")

# Check if queries_list is empty
if not queries_list:
    print("ERROR: queries_list is empty!")
    exit(1)

embeddings = model.encode(queries_list).tolist()
print(f"Generated {len(embeddings)} embeddings")

metadatas = [
    {'response': row['text'], 'query': row['query_text']}
    for _, row in pairs.iterrows()
]

# Add to collection
print("Adding to ChromaDB collection...")
collection.add(ids=ids, embeddings=embeddings, metadatas=metadatas)

print(f"Successfully added {len(ids)} query-response pairs to ChromaDB.")