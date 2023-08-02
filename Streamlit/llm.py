import os
os.environ["OPENAI_API_KEY"] = "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"

from langchain.llms import OpenAI
import streamlit as st

st.title('ChatGPT')
prompt = st.text_input('enter your prompt')

llm = OpenAI(temperature=0.9)

response = llm(prompt)

st.write(response)
