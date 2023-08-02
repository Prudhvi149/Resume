import os
os.environ["OPENAI_API_KEY"] = "Enter your key here"



from langchain.llms import OpenAI
import streamlit as st

st.title('ChatGPT')
Inputprompt = st.text_input('enter your prompt')

defaultInstruction = "you are a doctor"

prompt = defaultInstruction + ',' + Inputprompt

llm = OpenAI(temperature=0.9)

response = llm(prompt)

st.write(response)



