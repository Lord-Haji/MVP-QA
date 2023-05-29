import streamlit as st
import os
from app import AudioTranscription
from config import API_KEY

# Function to convert the string
# def convert_string(input_string):
#     characters_to_remove = [" ", ":", "-"]
#     converted_string = "".join([char.lower() for char in input_string if char not in characters_to_remove])
#     return converted_string

def main():
    api_key = API_KEY

    st.header("MVP - Quality Assurance")

    # Upload button
    audio_files = st.file_uploader("Upload Audio Files", type=["mp3", "wav"], accept_multiple_files=True)

    if audio_files:
        for i, audio_file in enumerate(audio_files):
            # Process each uploaded audio file
            file_name = os.path.splitext(audio_file.name)[0]
            audio_transcription = AudioTranscription(audio_file, file_name)

            transcript_text = ""

            # Transcribe and save
            with st.spinner("Transcribing audio {}...".format(i + 1)):
                transcript_text = audio_transcription.transcribe_and_save()

            # Display the transcription
            st.subheader("Transcription {}".format(i + 1))
            st.text_area("transcript_{}".format(i), value=transcript_text, key="transcript_text_{}".format(i))

            # Classify the call
            with st.spinner("Classifying audio {}...".format(i + 1)):
                classification = audio_transcription.classify_call()

            # Display the classification
            st.subheader("Classification {}".format(i + 1))
            st.text_area("classification_{}".format(i), value=classification, key="classification_{}".format(i))


            # Show "Send for Review" button when transcription is done
            if classification:
                if st.button("Send for Review {}".format(i + 1)):
                    # review_comment = st.text_input("Enter your review comment:")
                    with st.spinner("Reviewing audio {}...".format(i + 1)):
                        review_text = audio_transcription.qa_review()  # Call the function to submit the review
                    # st.success("Review submitted successfully!")  # Display success message

                    # Display the returned review
                    st.subheader("Review {}".format(i + 1))
                    st.text_area("Review Text {}".format(i + 1), value=review_text, key="review_text_{}".format(i)) 


if __name__ == "__main__":
    main()
