from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv

model = ChatOpenAI(model = "gpt-4",temperature=0.3, max_completion_token = 10)

result = model.invoke("what is the capital of India?")

print(result.content)



# anthropic
"""
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

model = ChatAnthropic(model= "<model name>")
result = model.invoke("what is the capital of India?")
print(result.content)
"""

# goole gemini
"""
formlangchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

model = ChatGoogleGenerativeAI(model= "<model name>")
result = model.invoke("what is the capital of India?")
print(result.content)
"""
