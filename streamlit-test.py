import os
import streamlit as st
from audioquery import AudioQuery
import pandas as pd

def main():

    st.header("MVP - Quality Assurance")

    # Upload button
    audio_file = st.file_uploader("Upload Audio File", type=["mp3", "wav"])

    if audio_file:
        # Process the uploaded audio file
        file_name = os.path.splitext(os.path.basename(audio_file.name))[0]
        audio_query = AudioQuery(audio_file, file_name)

        transcript_text = ""

        # Transcribe and save
        with st.spinner("Transcribing audio..."):
            transcript_text = audio_query.transcribe()

        # Display the transcription
        st.subheader("Transcription")
        st.text_area("transcription", value=transcript_text, key="transcript_text", height=calculate_height(transcript_text), label_visibility="hidden")

        # Button to classify call
        if st.button("Classify Call"):
            with st.spinner("Classifying call..."):
                classification = audio_query.classify_call()
                # st.text_area("classification", value=classification, key="classification")
                display_table(classification)

        # Button to extract data
        if st.button("Extract Data"):
            with st.spinner("Extracting data..."):
                data = audio_query.extract_data()
                display_table(data, transpose=True)

        # # Button to review transcription
        # if st.button("Review Transcription"):
        #     with st.spinner("Reviewing audio..."):
        #         review_text, score, status = audio_query.qa_review()

        #     st.subheader("QA Review")

        #     # call_data = "Calltype: " + calltype.strip() + "\n" + "Source: " + source + "\n" + "QA comment: " + status + "ed \n\n\n"

        #     # num_lines = call_data.count('\n') + data.count('\n') + 3  # Add 3 for extra lines

        #     st.text_area("Review", value=review_text, height=900)

        #     if status == "Pass":
        #         st.success(str(score) + "\t" + status, icon="✅")  # Display success message
        #     if status == "Fail":
        #         st.error(str(score) + "\t" + status, icon="❌")

def calculate_height(text, max_line_length=60, pixels_per_line=12):

    lines = len(text) // max_line_length
    return lines * pixels_per_line

def display_table(dictionary, transpose=False):
     # CSS to inject contained in a string
    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """

    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    if transpose:
        df = pd.DataFrame(list(dictionary.items()), columns=['Particulars', 'Information'])
        df.index += 1
        st.table(df)
    else:
        df = pd.DataFrame([dictionary])
        df.index += 1
        st.table(df)



if __name__ == "__main__":
    main()
