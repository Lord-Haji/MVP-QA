import os
import streamlit as st
from app import AudioTranscription

def main():

    st.header("MVP - Quality Assurance")

    # Upload button
    audio_file = st.file_uploader("Upload Audio File", type=["mp3", "wav"])

    if audio_file:
        # Process the uploaded audio file
        file_name = os.path.splitext(os.path.basename(audio_file.name))[0]
        audio_transcription = AudioTranscription(audio_file, file_name)

        transcript_text = ""

        # Transcribe and save
        with st.spinner("Transcribing audio..."):
            transcript_text = audio_transcription.transcribe()

        # Display the transcription
        st.subheader("Transcription")
        st.text_area("transcript", value=transcript_text, key="transcript_text", height=800)

        # Button to classify call
        if st.button("Classify Call"):
            with st.spinner("Classifying call..."):
                classification = audio_transcription.classify_call()
                st.text_area("Classification: ", value=classification, key="classification")

        # Button to extract data
        if st.button("Extract Data"):
            with st.spinner("Extracting data..."):
                data = audio_transcription.extract_data()
                st.text_area("Data: ", value=data, key="data", height = 500)

        # Button to review transcription
        if st.button("Review Transcription"):
            with st.spinner("Reviewing audio..."):
                review_text, score, status = audio_transcription.qa_review()

            st.subheader("QA Review")

            # call_data = "Calltype: " + calltype.strip() + "\n" + "Source: " + source + "\n" + "QA comment: " + status + "ed \n\n\n"

            # num_lines = call_data.count('\n') + data.count('\n') + 3  # Add 3 for extra lines

            st.text_area("Review", value=review_text, height=900)

            if status == "Pass":
                st.success(str(score) + "\t" + status, icon="✅")  # Display success message
            if status == "Fail":
                st.error(str(score) + "\t" + status, icon="❌")

if __name__ == "__main__":
    main()
