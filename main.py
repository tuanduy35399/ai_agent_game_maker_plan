from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage

load_dotenv()

model=ChatOpenAI(model="my_models", 
                 base_url="http://localhost:20128/v1", 
                 verbose=True, )

agent = create_agent(model=model, tools=[])

while True:
    content= input("You: ")
    
    if content == "0":
        break
    for token, metadata in agent.stream(
    {
        "messages": [HumanMessage(content="Xin chao ban")]
    }
    )