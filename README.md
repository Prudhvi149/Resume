# Introduction Workshop

Google Form:https://forms.gle/JP7NrrcCmtiAqFs1A

Portfolio websites:

Car game: https://bruno-simon.com/

Sanath Swaroop : https://sanathswaroop.com/

ashish :  https://ashish159565.github.io/PORTFOLIO/

https://github.com/ashish159565/PORTFOLIO




Free Udemy Course links:

Google Bard:  https://www.udemy.com/course/google-bard-masterclass-guide-for-beginners300-prompts/?couponCode=452406151151D445F69F

Chatgpt At Work : https://www.udemy.com/course/chatgpt-masterclass-be-a-superhero-at-work-with-chatgpt-q/?couponCode=A08C29C176E1CBCF2D13

Python Course : https://www.udemy.com/course/python-programming-for-beginners-python-programming-101/?couponCode=CCE240B77586D021F4BD

Web development Course : https://www.udemy.com/course/beginners-web-development-bundle-html-css-and-javascript/?couponCode=7AD3197D416B350DBA09



install langchain : pip install langchain[all]



Program1: 

import os
os.environ["OPENAI_API_KEY"] = "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"

from langchain.llms import OpenAI

prompt = input('ask your question')

llm = OpenAI(temperature=0.9)

response = llm(prompt)
print(response)


Program2: 
import os
os.environ["OPENAI_API_KEY"] = "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"
from langchain.llms import OpenAI

inputprompt = input('ask your question')

defalutprompt = "you are a chatbot"
prompt = inputprompt +','+ defalutprompt

llm = OpenAI(temperature=0.9)

response = llm(prompt)
print(response)
