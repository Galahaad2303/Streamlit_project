import streamlit as st
import speech_recognition as sr
from googletrans import Translator

def transcribe_and_translate(audio_file):
    r = sr.Recognizer()
    translator = Translator()

    with sr.AudioFile(audio_file) as source:
        st.info("Transcribing...")
        audio = r.record(source)

        try:
            text = r.recognize_google(audio, language="auto")
            detected_lang = translator.detect(text).lang
            st.success("Detected Language: " + detected_lang)
            st.write("Transcription:")
            st.write(text)

            translation = translator.translate(text, src=detected_lang, dest="en")
            st.success("English Translation:")
            st.write(translation.text)
        except sr.UnknownValueError:
            st.warning("Unable to recognize speech")
        except sr.RequestError as e:
            st.error(f"Error occurred; {e}")

# Streamlit UI
st.title("Speech-to-Text and Translation Generator")
st.write("Upload an audio file (in WAV or FLAC format) for transcription and translation to English.")

# Audio file upload
audio_file = st.file_uploader("Choose an audio file", type=["wav", "flac"])

if audio_file is not None:
    st.audio(audio_file, format="audio/wav", start_time=0)

    if st.button("Transcribe and Translate"):
        transcribe_and_translate(audio_file)
