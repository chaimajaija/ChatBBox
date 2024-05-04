import streamlit as st

import openai
import os
from openai import OpenAI

st.set_page_config(page_title="Find your Business Idea",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Brain storm problems 🤖")

input_text=st.text_input("Specify the sector")

## creating to more columns for additonal 2 fields


submit=st.button("Generate")

## Final response

os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']






# configure Azure OpenAI service client 
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY']
  )

#deployment=os.environ['OPENAI_DEPLOYMENT']
deployment="gpt-4"

# add your completion code
question = input_text
prompt = """
You are an expert investor & a problem solver gunius  an IQ of 200.

You find realword issue & turm them to business ideas.

Provide 10 problems for this sector {question}
"""
messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)



#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.

if submit:
    st.write(completion.choices[0].message.content)
