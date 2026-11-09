from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage
# from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
from tools import *
from photo_decoder import *
load_dotenv()

model=ChatOpenAI(model="my_models", 
                 base_url="http://localhost:20128/v1", 
                 verbose=True, )

config = {
    "configurable": {"thread_id": 1}
}
with SqliteSaver.from_conn_string("game_memory.db") as checkpointer:
    agent = create_agent(model=model, 
                        tools=[search_web, make_report, scrape_webpage],
                        checkpointer= checkpointer)

    while True:
        choice= input("Type 1 to chat/ Type 2 to upload img [1/2]: ")
        print("You: ")
        if choice == "1":
            message =  [HumanMessage(content=input())]
        if choice == "2":
            img_path= choose_image_file()
            prompt = input()
            message = build_image_message(image_path=img_path, prompt=prompt)
        if choice == "0":
            break
        print("Bot: ")
        for token, metadata in agent.stream(
        {
            "messages": message,
        }, stream_mode="messages", config=config
        ):
            if token.content:
                print(token.content, end="", flush=True)
        print("")