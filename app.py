import streamlit as st
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv
import os
from main2 import agent

st.title("💬 Chatbot")
st.write(
    "My name is Anas Drira i made this simple chatbot that uses Mistreal model to generate code."
    "this webpage is used for testing now "
)

st.title("code generator")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get completion from Mistral
    try:
        assistant_message = agent.chat(prompt)
    except :
        assistant_message="i'm not able to find answer to your query "
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(assistant_message)

    # Add assistant message to chat history
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})
