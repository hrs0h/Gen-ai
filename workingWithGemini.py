import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key="AIzaSyDJYeOm2DcAgHAXvmMN8N5l-XlLrBfDwOY")
prompt_template = PromptTemplate.from_template("Write a tweet about {topic}.")
chain = llm | prompt_template
response = chain.invoke("AI in healthcare")

print(response.to_messages())
