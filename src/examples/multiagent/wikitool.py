from smolagents import Tool
import wikipedia
import os 

class WikiTool(Tool):
    name = "wikipedia_search_tool"
    description = """This is a tool that allows a user to search across wikipedia"""
    inputs = {
        "query": {
            "type": "string",
            "description": "the query that you wish to search for",
        }
    }
    output_type = "string"
    
    def forward(self, query: str):
        return wikipedia.search(query)
