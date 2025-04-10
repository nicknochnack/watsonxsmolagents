# Smolagents using Llama 4
Check out how to build your own ReAct agent using Hugging Face smolagents and Llama 4 via watsonx.ai

## See it live and in action 📺
<img src="https://i.imgur.com/QMeKC8F.gif"/>

# Startup 🚀
1. Create a virtual environment `uv venv` and activate it `source .venv/bin/activate`
2. Update your `WATSONX_APIKEY` and `WX_PROJECT_ID` in the `.env` file.
3. Install dependencies `uv pip install -r pyproject.toml`
4. Runt the agent `uv run main.py`

# Agentic RAG
<img src="https://i.imgur.com/8WlekfU.gif"/>

## Steps to Run
1. Install chroma db `uv add chromadb`
2. Run `uv run src/examples/rag/rag.py`
3. Note if you want to reinstantiate the database you can run `uv run src/examples/rag/create_chroma.py` this will recreate the ticker_db chromadb instance
I've kept it pretty simple, it'll show how to find a stock ticker for a given company using the vector database. 

# Multi Modal
<img src="https://i.imgur.com/UATj5Mv.gif"/>

## Steps to Run
1. Install pillow to load an image `uv add pillow`
2. Run the image analysis example `uv run src/examples/multimodal/image.py`
This demonstrates how to extract drug label information from an image, something which we would have traditionally used OCR for. Works pretty well in this case.

# Multi Agent
<img src="https://i.imgur.com/sLGftx3.gif"/>

## Steps to Run
1. Pretty easy this one, just kick it off `uv run src/examples/multiagent/multiagent.py`
This will use a manager agent to kick off a task from a subordinate agent to do wikipedia research.

# Tracing 
<img src="https://i.imgur.com/YasWC80.gif"/>

## Steps to run 
1. Add telemetry `uv add "smolagents[litellm,telemetry]"`
2. Start arize phoenix server `uv run -m phoenix.server.main serve`
3. Access server at `http://0.0.0.0:6006`
4. Run agent with telemetry `uv run src/examples/tracing.py`

# Who, When, Why?

👨🏾‍💻 Author: Nick Renotte <br />
📅 Version: 1.x<br />
📜 License: This project is licensed under the MIT License </br>
