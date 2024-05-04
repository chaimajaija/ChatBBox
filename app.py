import streamlit as st
import os
from openai import OpenAI

# Set OpenAI API key from Streamlit secrets
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

# Configure Azure OpenAI service client
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

# Deployment
deployment = "gpt-4"

@st.experimental_memo
def get_answer(prompt, question):
    # Construct prompt
    prompt_text = f"{prompt}\nQuestion: {question}"
    messages = [{"role": "user", "content": prompt_text}]
    
    # Make completion request
    completion = client.chat.completions.create(model=deployment, messages=messages)
    
    try:
        # Extract the content from the response
