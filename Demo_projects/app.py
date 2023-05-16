import streamlit as st
import pyttsx3


def text_to_speech(text, voice):
    engine = pyttsx3.init()
    engine.setProperty("rate", 20)  # Adjust the speech rate (words per minute)
    engine.setProperty("voice", voice)  # Set the desired voice

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

def main():
    st.title("Text-to-Speech Conversion")

    # Get user input for text
    text = st.text_area("Enter the text you want to convert to speech")

    # Get available voices
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    voice_options = [voice.name for voice in voices]

    # Select voice
    selected_voice = st.selectbox("Select a voice", voice_options)

    # Convert text to speech
    if st.button("Generate Speech"):
        engine.save_to_file(text, 'output.mp3')
        engine.runAndWait()
        st.success("Speech generated successfully!")
        st.audio('output.mp3')

if __name__ == "__main__":
    main()
