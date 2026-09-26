import os

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI


load_dotenv()

llm = GoogleGenerativeAI(model="gemini-3.6-flash")

response = llm.invoke(
    "Who is the current president of India?"
)

print(response)
