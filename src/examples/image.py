# Dependencies
import os
from dotenv import load_dotenv
from smolagents import CodeAgent, LiteLLMModel, DuckDuckGoSearchTool, VisitWebpageTool 

#LLM
llm = LiteLLMModel(
    model_id="watsonx/meta-llama/llama-4-maverick-17b-128e-instruct-fp8", 
    api_key=os.environ['WATSONX_APIKEY'], 
    num_ctx=8162
)

agent = CodeAgent(tools=[DuckDuckGoSearchTool(),VisitWebpageTool()], model=llm)
agent.run("what is the height of the Sydney Harbour Bridge in km?")
