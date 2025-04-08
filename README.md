# Smolagents using Llama 4
Check out how to build your own ReAct agent using Hugging Face smolagents and Llama 4 via watsonx.ai

## See it live and in action 📺
<img src="https://i.imgur.com/QMeKC8F.gif"/>

# Startup 🚀
1. Create a virtual environment `uv venv` and activate it `source .venv/bin/activate`
2. Update your `WATSONX_APIKEY` and `WX_PROJECT_ID` in the `.env` file.
3. Install dependencies `uv pip install -r pyproject.toml`
4. Runt the agent `uv run main.py`

</br>
# Other References 🔗 </br>
- ToDo...maybe later

# RAG
<img src="https://i.imgur.com/YasWC80.gif"/>
1. Add telemetry `uv add "smolagents[litellm,telemetry]"`
2. Start arize phoenix server `uv run -m phoenix.server.main serve`
3. Access server at `http://0.0.0.0:6006`
4. Run agent with telemetry `uv run tracing.py`

# Tracing 
<img src="https://i.imgur.com/YasWC80.gif"/>
1. Add telemetry `uv add "smolagents[litellm,telemetry]"`
2. Start arize phoenix server `uv run -m phoenix.server.main serve`
3. Access server at `http://0.0.0.0:6006`
4. Run agent with telemetry `uv run tracing.py`

# Who, When, Why?

👨🏾‍💻 Author: Nick Renotte <br />
📅 Version: 1.x<br />
📜 License: This project is licensed under the MIT License </br>
