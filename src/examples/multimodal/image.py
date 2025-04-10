# Dependencies
import os
from dotenv import load_dotenv
from smolagents import CodeAgent, LiteLLMModel, DuckDuckGoSearchTool, VisitWebpageTool 
from PIL import Image

image_path = os.path.join(os.path.dirname(__file__), "druglabel.png")
image = Image.open(image_path)

#LLM
llm = LiteLLMModel(
    model_id="watsonx/meta-llama/llama-4-maverick-17b-128e-instruct-fp8", 
    api_key=os.environ['WATSONX_APIKEY'], 
    num_ctx=8162
)

agent = CodeAgent(tools=[], model=llm)
agent.run("what drug is shown in the image? and also summarise the active ingredients", images=[image])
