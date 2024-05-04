import streamlit as st

import openai
import os
from openai import OpenAI

# Set OpenAI API key from Streamlit secrets
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

# Configure Azure OpenAI service client
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

# Deployment
deployment = "gpt-4"

def get_answer(prompt, question):
    # Construct prompt
    prompt_text = f"{prompt}\nQuestion: {question}"
    messages = [{"role": "user", "content": prompt_text}]
    
    # Make completion request
    completion = client.chat.completions.create(model=deployment, messages=messages)
    return completion["choices"][0]["message"]["content"]

def main():
    st.title("Interactive Prompt & Answer App")

    # Text input for the initial prompt
    prompt = st.text_input("Enter your prompt:")

    if prompt:
        # Text input for the question
        question = st.text_input("Enter your question:")

        if st.button("Get Answer"):
            # Get the answer based on the prompt and question
            answer = get_answer(prompt, question)
            st.write(f"Answer: {answer}")

            # Text input for the next prompt based on the answer
            next_prompt = st.text_input("Enter next prompt based on the answer:")
            
            if st.button("Get Answer for Next Prompt"):
                # Get the answer for the next prompt
                next_answer = get_answer(next_prompt, question)
                st.write(f"Answer for Next Prompt: {next_answer}")

if __name__ == "__main__":
    main()
