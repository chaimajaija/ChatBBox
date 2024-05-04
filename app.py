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

    # Text input for the initial prompt
    prompt = st.text_input("Enter your prompt:")

    if prompt:
        # Text input for the question
        question = st.text_input("Enter your question:")

        if st.button("Get Answer", key="get_answer_button"):
            # Get the answer based on the prompt and question
            answer = get_answer(prompt, question)
            st.write(f"Answer: {answer}")

            # Text input for the next prompt based on the answer
            next_prompt = st.text_input("Enter next prompt based on the answer:")

            # Use JavaScript to handle button click without form submission
            next_answer_button = st.button("Get Answer for Next Prompt", key="next_answer_button", help="next_answer_button")
            if next_answer_button:
                st.markdown(
                    """
                    <script>
                        document.getElementById("next_answer_button").formEnctype = "application/json";
                        document.getElementById("next_answer_button").formMethod = "get";
                        document.getElementById("next_answer_button").formAction = "javascript:void(0)";
                        document.getElementById("next_answer_button").onclick = function() {document.dispatchEvent(new Event("next_answer_button_clicked"))};
                    </script>
                    """,
                    unsafe_allow_html=True,
                )

                # Get the answer for the next prompt
                next_answer = get_answer(next_prompt, question)
                st.write(f"Answer for Next Prompt: {next_answer}")

if __name__ == "__main__":
    main()
