from langchain.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv


load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")

message = [
    SystemMessage(content=" You are a helpful assistant"),
    HumanMessage(content="Tell me about Langchain in short")
]

result = model.invoke(message)
message.append(AIMessage(content=result.content))

print(message)