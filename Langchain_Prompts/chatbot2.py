# This is upgraded version of previous chatbot with history

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()
model = ChatGroq(model="openai/gpt-oss-20b")
chat_history = [
    SystemMessage(content="You are cricket expert")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content= user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print(chat_history)