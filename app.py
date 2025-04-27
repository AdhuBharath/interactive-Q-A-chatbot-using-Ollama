import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import os

from dotenv import load_dotenv
load_dotenv()

os.environ["Langchain_api_key"] = os.getenv("Langchain_api_key")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot with ollama"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a coding master and an helpful assistance try to give me answers for the given questions"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,engine,temperature,max_tokens):

    llm=Ollama(model=engine)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({"question":question})
    return answer

engine=st.sidebar.selectbox("select your model",["gemma3:1b","moondream"])

temperature = st.sidebar.slider("Temperature",min_value=0.0,max_value=10.0,value=0.6)
max_tokens = st.sidebar.slider("max_tokens",min_value=50,max_value=300,value=150)

st.title("Q&A CHATBOT USING OLLAMA")

st.write("enter your query")
user_input = st.text_input("you:")

if user_input :
    response=generate_response(user_input,engine,temperature,max_tokens)
    st.write(response)
else:
    st.write("provide your query")

