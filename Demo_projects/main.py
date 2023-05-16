import streamlit as st
import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Adjust the speech rate (words per minute)

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

def main():
    st.title("Text-to-Speech Generator")

    # Get user input for text
    text = st.text_area("Enter the text you want to convert to speech")

    # Convert text to speech
    if st.button("Convert"):
        text_to_speech(text)
        st.success("Conversion complete! Check your speaker for audio output.")

if __name__ == "__main__":
    main()