from langchain.tools import tool
from tavily import TavilyClient
from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv


load_dotenv()
tavily_client=TavilyClient()
@tool
def search_web(query:str) -> Dict[str, Any]:
    """
    This tool use for searching information on the internet
    """
    print(f"Searching on {query}....")
    return tavily_client.search(query=query)

@tool
def make_report(content: str, name_file: str)-> str:
    """
    This tool use for making report .md type with content which was researched from search_web tool
    """
    path = Path(f"report/{name_file}.md")
    path.write_text(data=content, encoding="utf-8")

    return f"Report is saved at {path.resolve()}"
