import streamlit as st
import requests
import uuid

# Function to generate a unique session ID
def get_session_id():
    if 'session_id' not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())
    return st.session_state.session_id

# Streamlit app title
st.title("Bistro AI Assistant")

# Get or generate session ID
session_id = get_session_id()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Make a request to the FastAPI backend
    try:
        response = requests.post(
            "http://localhost:8000/agent/generate/chat/customer_support_agent",
            json={"query": prompt, "session_id": session_id}
        )
        response.raise_for_status()  # Raise an exception for bad status codes
        chat_response = response.json()
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": chat_response["response"]})
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(chat_response["response"])

    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")