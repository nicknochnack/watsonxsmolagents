
import os 
from dotenv import load_dotenv
from smolagents import CodeAgent, LiteLLMModel
from wikitool import WikiTool

load_dotenv()

#LLM
llm = LiteLLMModel(
    model_id="watsonx/meta-llama/llama-4-maverick-17b-128e-instruct-fp8", 
    api_key=os.environ['WATSONX_APIKEY'], 
    num_ctx=8162,
)

wiki_agent = CodeAgent(
    tools=[WikiTool()],
    model=llm,
    max_steps=10,
    name="wiki_search_agent",
    description="Can search wikipedia for you.",
)


manager_agent = CodeAgent(
    tools=[],
    model=llm,
    managed_agents=[wiki_agent],
)

manager_agent.run('Tell me about the development of the lightbulb?') 
