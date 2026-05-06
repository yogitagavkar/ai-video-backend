import streamlit as st
import requests

API_URL = "https://ai-video-text-summarization.onrender.com/process-video"
# For deployed:
# API_URL = "https://ai-video-text-summarization.onrender.com/process-video"

st.set_page_config(page_title="AI Video Processor", layout="wide")

st.title("🎬 AI Video Processing Platform")
st.markdown("Upload video → Get transcription + AI summary")

# Upload
uploaded_file = st.file_uploader("Upload Video", type=["mp4", "mov"])

if uploaded_file:
    st.video(uploaded_file)

    if st.button("🚀 Process Video"):
        with st.spinner("Processing... please wait ⏳"):

            files = {"file": uploaded_file.getvalue()}

            try:
                response = requests.post(
                    API_URL,
                    files={"file": (uploaded_file.name, uploaded_file.getvalue())}
                )

                if response.status_code == 200:
                    data = response.json()

                    st.success("✅ Processing Complete")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.subheader("📝 Transcription")
                        st.write(data["transcription"])

                    with col2:
                        st.subheader("📌 Summary")
                        st.write(data["summary"])

                else:
                    st.error(f"Error: {response.text}")

            except Exception as e:
                st.error(f"Failed to connect: {e}")