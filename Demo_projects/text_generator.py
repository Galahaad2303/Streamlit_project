import streamlit as st
import speech_recognition as sr

def transcribe_audio(audio_file):
    r = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        st.info("Transcribing...")
        audio = r.record(source)

        try:
            text = r.recognize_google(audio)
            st.success("Transcription:")
            st.write(text)
        except sr.UnknownValueError:
            st.warning("Unable to recognize speech")
        except sr.RequestError as e:
            st.error(f"Error occurred; {e}")

# Streamlit UI
st.title("Speech-to-Text Generator")
st.write("Upload an audio file (in WAV or FLAC format) for transcription.")

# Audio file upload
audio_file = st.file_uploader("Choose an audio file", type=["wav", "flac"])

if audio_file is not None:
    st.audio(audio_file, format="audio/wav", start_time=0)

    if st.button("Transcribe"):
        transcribe_audio(audio_file)
