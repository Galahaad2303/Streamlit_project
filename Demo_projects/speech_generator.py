import streamlit as st
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Female voice
female_voice = voices[1]
engine.setProperty('voice', female_voice.id)

# Male voice
male_voice = voices[0]

# Streamlit app layout
st.title("Text-to-Speech Web App")
st.write("***Enter text you wish convert into speech***")

# Voice selection
voice_selection = st.selectbox("***Select voice***", ("Female", "Male"))

# Text input feature
text = st.text_area("***Enter text here:***")

# Speech generation
if st.button("Generate Speech"):
    if voice_selection == "Female":
        engine.setProperty('voice', female_voice.id)
    elif voice_selection == "Male":
        engine.setProperty('voice', male_voice.id)

    engine.save_to_file(text, 'output.mp3')
    engine.runAndWait()
    st.success("Speech generated successfully!")
    st.audio('output.mp3')
