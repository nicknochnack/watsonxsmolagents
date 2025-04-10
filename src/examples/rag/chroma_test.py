import chromadb
import json

chroma_client = chromadb.PersistentClient(path="ticker_db")
collection = chroma_client.get_collection(name="stock_tickers")
results = collection.query(query_texts=["Astra"], n_results=2) 
print(results) 