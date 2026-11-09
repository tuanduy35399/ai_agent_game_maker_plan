from langchain.tools import tool
from tavily import TavilyClient
from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv
import json
import urllib.request
import urllib.error
import re
from html.parser import HTMLParser

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
    print(f"Dang tao bao cao: {name_file}")
    path = Path(f"report/{name_file}.md")
    path.write_text(data=content, encoding="utf-8")

    return f"Report is saved at {path.resolve()}"

# @tool 
# def create_new_tool(code: str, file_name:str):
#     """
#     Ham nay keu AI tu tao 1 tool
#     """
#     print(f"Dang tao 1 tool moi ten la: {file_name}")
#     path = Path(f"tools/{file_name}.py")
#     path.write_text(data=code)


class SimpleHTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []
        self.ignore_tags = {'script', 'style', 'head', 'title', 'meta', '[document]', 'noscript'}
        self.current_ignore = False
        self.ignore_stack = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() in self.ignore_tags:
            self.ignore_stack.append(tag.lower())
            self.current_ignore = True

    def handle_endtag(self, tag):
        if tag.lower() in self.ignore_tags and self.ignore_stack:
            self.ignore_stack.pop()
            if not self.ignore_stack:
                self.current_ignore = False

    def handle_data(self, data):
        if not self.current_ignore:
            text = data.strip()
            if text:
                self.result.append(text)

    def get_text(self):
        return "\n".join(self.result)

@tool
def scrape_webpage(url: str, max_chars: int = 8000) -> str:
    """
    Cao du lieu van ban thuan tu mot URL bat ky (su dung thu vien chuan Python, khong can cai them package ngoai).
    
    Args:
        url: Dia chi trang web can cao (vi du: 'https://example.com').
        max_chars: So ky tu toi da muon lay de tranh tran context (mac dinh 8000).
        
    Returns:
        Chuoi JSON chua ket qua: status, url, text trich xuat hoac error message.
    """
    print(f"Dang cao du lieu tu url: {url[:50]}...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            charset = response.headers.get_content_charset() or 'utf-8'
            html_content = response.read().decode(charset, errors='replace')
            
            parser = SimpleHTMLTextExtractor()
            parser.feed(html_content)
            extracted_text = parser.get_text()
            
            # Cat gon van ban theo gioi han
            truncated_text = extracted_text[:max_chars]
            
            return json.dumps({
                "status": "success",
                "url": url,
                "length": len(truncated_text),
                "content": truncated_text
            }, ensure_ascii=False)
            
    except Exception as e:
        return json.dumps({
            "status": "error",
            "url": url,
            "error": str(e)
        }, ensure_ascii=False)

