import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="./chroma"))

collection = client.get_or_create_collection("chapters")

def save_version(text, version_name):
    collection.add(documents=[text], ids=[version_name])

def search_content(query):
    return collection.query(query_texts=[query], n_results=1)
