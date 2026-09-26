from langchain_groq import ChatGroq
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")

result = model.invoke("who is the pm of India")
print(result.text)