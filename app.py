import streamlit as st
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ["MISTRAL_API_KEY"]

st.title("💬 Chatbot")
model = "mistral-large-latest"
st.write(
    "My name is Anas Drira i made this simple chatbot that uses Mistreal model to generate code."
    "this webpage is used for testing now "
)




if not api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:

    client = MistralClient(api_key=api_key)

    st.title("code generator")

    # Set a default model
    if "mistral_model" not in st.session_state:
        st.session_state["mistral_model"] = model

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
        chat_response = client.chat(
            model=st.session_state["mistral_model"],
            messages=[
                ChatMessage(role="user", content=prompt)
            ]
        )
        assistant_message = chat_response.choices[0].message.content

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(assistant_message)

        # Add assistant message to chat history
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})
