from langchain_groq import ChatGroq
from langchain.messages import HumanMessage,SystemMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv

load_dotenv()

chat_temp = ChatPromptTemplate([
    ("system","You are a {domain} experts"),
    ("human","explain the {topic} in medium lenght")
    #SystemMessage(content="You are a {domain} experts"),
    #HumanMessage(content="explain the {topic} in medium lenght")
])


    
    
prompt = chat_temp.invoke({"domain":"cricket", "topic":"virat kohli"})

print(prompt)