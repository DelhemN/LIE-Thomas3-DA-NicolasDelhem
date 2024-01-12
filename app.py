from langchain_community.llms import Ollama
import streamlit as st

# Instantiate the Ollama model
llm = Ollama(model="codellama")

# Streamlit app
st.title("Ollama Code Generation")

# User input for the prompt
prompt = st.text_input("Enter your programming prompt:")

# Button to generate response
if st.button("Generate Code"):
    # Invoke Ollama with user input
    response = llm.invoke(prompt)

    # Display the generated code
    st.code(response, language='python')
