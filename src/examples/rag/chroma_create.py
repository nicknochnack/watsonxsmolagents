import chromadb
import json

chroma_client = chromadb.PersistentClient(path="ticker_db")
try:
    collection = chroma_client.get_collection(name="stock_tickers")
except: 
    print('Collection does not exist')
    collection = chroma_client.create_collection(name="stock_tickers")

with open('chroma_tickers.json', 'r') as f: 
    tickers = json.load(f) 

data = {id:f"{ticker['ticker']} - {ticker['title']}" for id, ticker in tickers.items()}

add_stuff1 = collection.add(
    documents=list(data.values())[:5000],
    ids=list(data.keys())[:5000]
)

add_stuff2 = collection.add(
    documents=list(data.values())[5000:],
    ids=list(data.keys())[5000:]
)
print(collection) 
# results = collection.query(query_texts=["Microsoft"], n_results=2) 

# print('Final Results') 