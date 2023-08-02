import os
os.environ["OPENAI_API_KEY"] = "place key here"

from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)

while True:
    prompt = input('Ask your question (type "exit" to stop): ')
    
    if prompt.lower() == 'exit':
        break

    response = llm(prompt)
    print(response)
