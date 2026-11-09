from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage
# from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
from tools import *

load_dotenv()

model=ChatOpenAI(model="my_models", 
                 base_url="http://localhost:20128/v1", 
                 verbose=True, )

config = {
    "configurable": {"thread_id": 1}
}
with SqliteSaver.from_conn_string("game_memory.db") as checkpointer:
    agent = create_agent(model=model, tools=[search_web,make_report], checkpointer= checkpointer)

    while True:
        content= input("You: ")
        
        if content == "0":
            break
        print("Bot: ")
        for token, metadata in agent.stream(
        {
            "messages": [HumanMessage(content=content)]
        }, stream_mode="messages", config=config
        ):
            if token.content:
                print(token.content, end="", flush=True)
        print("")