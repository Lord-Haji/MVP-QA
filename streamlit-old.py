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
        # st.text_area("transcript", value=transcript_text, key="transcript_text", height=800)
        st.write(transcript_text)

        # Show "Send for Review" button when transcription is done
        if transcript_text:
            if st.button("Send for Review"):
                # Start the loading spinner
                with st.spinner("Reviewing audio..."):
                    classification = audio_transcription.classify_call()
                    data = audio_transcription.extract_data()
                    review_text, score, status = audio_transcription.qa_review()  # Call the function to submit the review

                # Display the returned review
                # st.subheader("Review")
                # st.text_area("Review Text", value=review_text, key="review_text")
                st.subheader("QA Review")
                calltype, source = classification.split(":")

                call_data = "Calltype: " + calltype.strip() + "\n" + "Source: " + source + "\n" + "QA comment: " + status + "ed \n\n\n"

                data += "\n\n"

                # st.write(call_data + data)

                st.text_area("review", value=(call_data + data + review_text), height = 1000)


                if status == "Pass":
                    st.success(str(score) + "\t" +  status, icon="✅")  # Display success message
                if status == "Fail":
                    st.error(str(score) + "\t" +  status, icon="❌")


if __name__ == "__main__":
    main()
