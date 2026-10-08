from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage

chat_temp= ChatPromptTemplate([
    ("system", "You are a helpful customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human",'{query}')
])



chat_history = [
    HumanMessage(content="I want to request a refund for my order #12345."),
    AIMessage(
        content="Your refund request for order #12345 has initiated. "
        "It will be processed in 3-5 business days."
    ),
]

prompt = chat_temp.invoke({"chat_history":chat_history, "query":"where is my refund"})

print(prompt)
