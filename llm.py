import os
os.environ["OPENAI_API_KEY"] = "enter key here"

from langchain.llms import OpenAI

prompt = input('ask your question :')

llm = OpenAI(temperature=0.9)

response = llm(prompt)

print(response)
