import os
from dotenv import load_dotenv
from smolagents import CodeAgent, LiteLLMModel
from tool import StockTickerRAG

load_dotenv()
stock_ticker_rag = StockTickerRAG()

#LLM
llm = LiteLLMModel(
    model_id="watsonx/meta-llama/llama-4-maverick-17b-128e-instruct-fp8", 
    api_key=os.environ['WATSONX_APIKEY'], 
    num_ctx=8162
)

agent = CodeAgent(
    tools=[stock_ticker_rag], model=llm, max_steps=4, verbosity_level=2
)

agent.run('what is the stock ticker for Bank of America?')