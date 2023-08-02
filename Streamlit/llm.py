import os
os.environ["OPENAI_API_KEY"] = "enter your api key here"

from langchain.llms import OpenAI
import streamlit as st

st.title('ChatGPT')
prompt = st.text_input('enter your prompt')

llm = OpenAI(temperature=0.9)

response = llm(prompt)

st.write(response)
