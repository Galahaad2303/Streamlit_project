import streamlit as st
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set the voice to a female voice (change the index based on available voices)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Streamlit app layout
st.title("Text-to-Speech Web App")
st.write("Enter text to convert to speech")

# Text input feature
text = st.text_area("Enter text here")

# Speech generation
if st.button("Generate Speech"):
    engine.save_to_file(text, 'output.mp3')
    engine.runAndWait()
    st.success("Speech generated successfully!")
    st.audio('output.mp3')
