import streamlit as st

import openai
import os


Key=st.secrets('API_KEY')
os.environ["OPENAI_API_KEY"] = Key
model=os.environ["OPENAI_API_KEY"]
question = input("Ask your questions on python language to your study buddy: ")
prompt = f"""
You are an expert on the python language.

Whenever certain questions are asked, you need to provide response in below format.

- Concept
- Example code showing the concept implementation
- explanation of the example and how the concept is done for the user to understand better.

Provide answer for the question: {question}
"""
messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=model, messages=messages)




st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text=st.text_input("Enter the Blog Topic")

## creating to more columns for additonal 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Researchers','Data Scientist','Common People'),index=0)
    
submit=st.button("Generate")

## Final response
if submit:
    st.write(completion.choices[0].message.content)
