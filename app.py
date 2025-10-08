import streamlit as st
import requests
import uuid
import json

st.set_page_config(
    page_title="Bistro AI Assistant",
    page_icon="🧑‍🍳",
    layout="wide"
)

st.title("🧑‍🍳 Bistro AI Assistant")
st.markdown("""
Welcome to the Bistro AI Assistant! I can help you with questions about our menu, assist with reservations, or take note of any complaints.
How can I help you today?
""")


FASTAPI_URL = "http://127.0.0.1:8000/agent/generate/chat/customer_support_agent"

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Chat Controls")
    if st.button("🔄 New Chat"):
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.messages = []
        st.rerun()

    st.info(f"**Current Session ID:**\n`{st.session_state.session_id}`")
    st.markdown("---")
    st.markdown("""
    **About:**
    This chat interface allows you to interact with the Bistro AI Assistant, built with LangGraph and Streamlit.
    """)


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        content_to_display = message["content"]
        if message["role"] == "assistant":
            content_to_display = content_to_display.replace('\n', '  \n')
        st.markdown(content_to_display)

if prompt := st.chat_input("What would you like to know?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                payload = {
                    "query": prompt,
                    "session_id": st.session_state.session_id
                }
                headers = {"Content-Type": "application/json"}

                response = requests.post(
                    FASTAPI_URL,
                    data=json.dumps(payload),
                    headers=headers,
                    timeout=120
                )

                response.raise_for_status()

                response_data = response.json()
                ai_response = response_data.get("response", "Sorry, I encountered an error and couldn't get a response.")

                formatted_response = ai_response.replace('\n', '  \n')
                st.markdown(formatted_response)
                st.session_state.messages.append({"role": "assistant", "content": ai_response})

            except requests.exceptions.RequestException as e:
                error_message = f"Could not connect to the agent. Please make sure the backend is running. \n\n**Error:** {e}"
                st.error(error_message)
                st.session_state.messages.append({"role": "assistant", "content": error_message})
            except Exception as e:
                error_message = f"An unexpected error occurred: {e}"
                st.error(error_message)
                st.session_state.messages.append({"role": "assistant", "content": error_message})

