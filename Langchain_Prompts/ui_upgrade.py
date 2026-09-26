from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt

import streamlit as st

load_dotenv()
model = ChatGroq(model="openai/gpt-oss-20b")
template = load_prompt('Langchain_Prompts/template.json')


st.header("Research Tool")

paper_input =st.selectbox("Select Research Paper Name",["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )



prompts = template.invoke({
    "paper_input" : paper_input,
    "style_input":style_input,
    "length_input":length_input
})

if st.button("Summarize"):
    result = model.invoke(prompts)
    st.write(result.content)