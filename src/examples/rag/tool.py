from smolagents import Tool
import chromadb

class StockTickerRAG(Tool):
    name = "stock_ticker_rag"
    description = """This is a tool that returns the most likely stock ticker and description based on a query to a vector database. """
    inputs = {
        "stock_name": {
            "type": "string",
            "description": "the stock name e.g. Nvidia or Bank of America",
        }
    }
    output_type = "string"

    def __init__(self, **kwargs): 
        super().__init__(**kwargs)
        self.chroma_client = chromadb.PersistentClient(path="ticker_db")
        self.collection = self.chroma_client.get_collection(name="stock_tickers")
    
    def forward(self, stock_name: str):
        return self.collection.query(query_texts=[stock_name], n_results=1) 
