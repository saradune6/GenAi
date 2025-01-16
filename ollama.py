import os
from dotenv import load_dotenv  
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


## prompt template 
prompt=ChatPromptTemplate.from_messages(
    [
        ("system",'You are a helpful assiatant , Please respond to the following questions'),
        ('user','Question:{question}')
    ]
)

## Streamlit framework
st.title("Langchain demo with gemma")
input_text = st.text_input("Enter your question here")


## call ollama model
llm=Ollama(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))