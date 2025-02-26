import streamlit as st  # Import Streamlit for UI development
import requests  # Import requests to send API requests

# Set up the Streamlit page configuration
st.set_page_config(page_title="LangGraph Agent UI", layout="centered")

# Define the API endpoint for the chatbot backend
API_URL = "http://127.0.0.1:8000/chat"

# Available model options for the user to select
MODEL_NAMES = [
    "llama3-70b-8192",
    "mixtral-8x7b-32768"
]

# Title and description for the Streamlit UI
st.title("LangGraph Chatbot Agent")
st.write("Interact with the LangGraph-based agent using this interface")

# User input fields
given_system_prompt = st.text_area("Define your AI Agent: ", height=70, placeholder="Type your system prompt here...")
selected_model = st.selectbox("Select Model", MODEL_NAMES)  # Dropdown to select the AI model
user_input = st.text_area("Enter your message(s): ", height=150, placeholder="Type your message here...")

# Button to submit the request
if st.button("Submit"):
    if user_input.strip():  # Ensure input is not empty
        try:
            # Prepare the request payload
            payload = {
                "messages": [user_input],
                "model_name": selected_model,
                "system_prompt": given_system_prompt
            }

            # Send the POST request to the API
            response = requests.post(API_URL, json=payload)

            # Handle the API response
            if response.status_code == 200:
                response_json = response.json()

                # Check if there is an error in the response
                if "error" in response_json:
                    st.error(response_json["error"])
                else:
                    # Extract AI response messages
                    ai_response = [
                        message.get("content", "")
                        for message in response_json.get("messages", [])
                        if message.get("type") == "ai"
                    ]

                    # Display the AI response if available
                    if ai_response:
                        st.subheader("Agent Response:")
                        st.markdown(f"Final Response: {ai_response[-1]}")
                    else:
                        st.warning("No response received")
            else:
                st.error(f"Response failed with status code: {response.status_code}")

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a message before submitting")  # Show warning if input is empty
