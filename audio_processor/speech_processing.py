import speech_recognition as sr
import streamlit as st
import sounddevice as sd
from TTS.api import TTS


def speech_recognizer():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # st.info("Listening...")
        audio = r.listen(source, timeout=10)
        try:
            query = r.recognize_google(audio, language="en_in")
            return query.lower()
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"



def text_to_speech(text, device):
    tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False).to(device)
    wav = tts.tts(text=text, speaker="p266")
    sd.play(wav, samplerate=22050)
    sd.wait()