import streamlit as st
import torch
from dotenv import load_dotenv
import openai
import os

from audio_processor.speech_processing import text_to_speech, speech_recognizer
from gen_response.bot_output import teacher_response

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key
 
device = "cuda" if torch.cuda.is_available() else "cpu"
    


def initialize_session_state():
    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []

def update_conversation_history(user_input, bot_response):
    st.session_state.conversation_history.append({"user_input": user_input, "bot_response": bot_response})


def main():
    load_dotenv()
    initialize_session_state()
    
    st.set_page_config(page_title="English Learner Chatbot", page_icon=":speech_balloon:")
    st.title("English Learner Chatbot")

    st.sidebar.subheader("Press speak button while speaking, Thankyou")
    if st.sidebar.button("Speak"):
       
        user_input = speech_recognizer()
        bot_response = teacher_response(openai, user_input)
        text_to_speech(bot_response, device)
        
        update_conversation_history(user_input, bot_response)


    for i, entry in enumerate(st.session_state.conversation_history):
        st.text_area("User:", value=entry["user_input"], height=100, max_chars=1000, key=f"user_{i}")
        st.text_area("Chatbot:", value=entry["bot_response"], height=100, max_chars=1000, key=f"bot_{i}")



if __name__ == "__main__":
    main()
