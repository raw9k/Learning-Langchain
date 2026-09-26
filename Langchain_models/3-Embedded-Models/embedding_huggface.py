from langchain_huggingface import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

text = "France fails to win world cup"

vec= embeddings.embed_query(text)
print(str(vec))