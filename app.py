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
        answer = completion.choices[0].message.content
        return answer
    except AttributeError:
        # Handle unexpected response format
        st.error("Error: Unexpected response format. Please try again.")
        return None
    except Exception as e:
        # Handle other exceptions
        st.error(f"Error: {str(e)}")
        return None

def main():
    st.title("Interactive Prompt & Answer App")

    # Stage 1: Input prompt and question
    if 'stage' not in st.session_state:
        st.session_state.stage = 1
    if st.session_state.stage == 1:
        prompt = st.text_input("Enter your prompt:")
        st.session_state.question = st.text_input("Enter:")
        if st.button("Get Answer"):
            st.session_state.answer = get_answer(prompt, st.session_state.question)
            st.session_state.stage = 2
    
    # Stage 2: Display answer and input next prompt
    elif st.session_state.stage == 2:
        st.write(f"Answer: {st.session_state.answer}")
        next_prompt = st.text_input("Enter next prompt based on the answer:")
        if st.button("Get Answer for Next Prompt"):
            st.session_state.answer = get_answer(next_prompt, st.session_state.question)

if __name__ == "__main__":
    main()
