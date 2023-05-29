import os
import openai
from time import time
import re
from database import fetch_transcription, cache_transcription
from qagpt_test import generate_report
from classify import classify_call
# from score_calculator import calculate_score
from config import API_KEY

from scores import scores_dict


class AudioTranscription:
    def __init__(self, audio_file, file_name):
        self.audio_file = audio_file
        self.file_name = file_name
        self.transcript = ""
        self.call_category = ""
        self.report = []

    @staticmethod
    def timer(func):
        def wrap_func(*args, **kwargs):
            t1 = time()
            result = func(*args, **kwargs)
            t2 = time()
            print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
            return result
        return wrap_func

    @timer
    def transcribe(self):
        transcript_text = fetch_transcription(self.file_name)

        if transcript_text:
            # Return cached transcription
            self.transcript = transcript_text
        else:
            openai.api_key = API_KEY
            transcript_text = openai.Audio.transcribe("whisper-1", self.audio_file)["text"]
            # Cache the transcription in the database
            cache_transcription(self.file_name, transcript_text)
            self.transcript = transcript_text

        return transcript_text

    def transcribe_and_save(self):
        transcript_text = self.transcribe()

        folder_name = "transcripts"
        file_path = os.path.join(folder_name, f"{self.file_name}.txt")

        os.makedirs(folder_name, exist_ok=True)

        with open(file_path, 'w') as file:
            file.write(transcript_text)

        # with open(f"{self.file_name}.txt", 'w') as file:
        #     file.write(transcript_text)
        return transcript_text

    @timer
    def classify_call(self):
        # transcript_text = self.transcribe()
        self.call_category = classify_call(self.transcript)
        return self.call_category

    def qa_review(self):
        # self.transcribe()
        self.classify_call()
        report = self.call_category + "\n"

        # Standardize Call Category string since GPT-3.5-Turbo Doesnt generate uniform results as of 24-05-23
        characters_to_remove = [" ", ":", "-", ","]
        converted_string = re.sub(r'\(.*?\)', '', self.call_category)
        converted_string = "".join([char.lower() for char in converted_string if char.isalnum() and char not in characters_to_remove])

        print(converted_string)
        report += generate_report(self.transcript, converted_string)
        self.report = report


        true_lines = [line for line in self.report.splitlines() if 'True' in line]
        true_numbers = [re.search(r'(\d+)\.', line).group(1) for line in true_lines]
        true_numbers = [int(num) for num in true_numbers]

        print(true_numbers)
        # report += true_numbers

        total_score = sum(scores_dict.get(converted_string, [0])[param - 1] for param in true_numbers)


        # report += "\n" + str(total_score) + "\t"

        if total_score >= 80:
            status = "Pass"
                
        else:
            status = "Fail"

        # print(report)


        return report, total_score, status

    # def generate_output(self):
    #     self.qa_review()
    #     calculate_score()


# Rest of your code...

def main():
    audio_file_name = "audio/movein_2.mp3"
    

    file_name = os.path.splitext(os.path.basename(audio_file_name))[0]

    with open(audio_file_name, "rb") as audio_file:
        audio_transcription = AudioTranscription(audio_file, file_name)
        print(audio_file)
        print(audio_transcription.classify_call())
        print(audio_transcription.qa_review())

        # audio_transcription.generate_output()

    # print(f"Transcript: {transcript}")
    # print(f"Points: {points}")

if __name__ == "__main__":
    main()

