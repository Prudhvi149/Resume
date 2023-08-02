import os
os.environ["OPENAI_API_KEY"] = "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"

from langchain.llms import OpenAI

prompt = input('ask your question :')

llm = OpenAI(temperature=0.9)

response = llm(prompt)

print(response)
