import os
import openai

from config import API_KEY

openai.api_key = API_KEY



def extract_data(transcript):


    extract_prompt = """
    The topics that needs extraction is mentioned below delimited with triple backticks

    ```
    Current customer: Yes/No/Unsure
    Life Support: YES/NO


    Name
    DOB: Date of Birth in DD/MM/YYYY format
    Contact Number
    Email
    Postal Address
    Solar: YES/NO
    Delivery method

    Did Agent confirm OTP (current customer only):

    Concession Card
    Issue Date
    Expiry Date

    Secondary Account Holder Name
    DOB

    Contact Number

    Billing cycle offered

    Promotions mentioned

    Supply Address
    NMI
    MIRN

    Business name / Account name
    ABN


    MOVE IN FEE: 
    Date of move in or Connection
    Power State: off/ On
    Advised clear access for connection : Yes/No
    ```
    If the data is not captured in the transcript the value should be "NOT CAPTURED"

    Step 1: Extract all the data mentioned here from the transcript

    Your Output should be a JSON object with the keys being the data that needs to be extracted and values being the extracted data
    """


    messages = [
        {
            "role": "system",
            "content": f"Hello GPT, I have a call transcript that I'd like you to extract data from. Here is the transcript: '{transcript}'"
        },
        {"role": "user", "content": extract_prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
        temperature=0,
        max_tokens=400,
    )

    return response["choices"][0]["message"]["content"].strip()

# Example usage
# file_path = 'transcripts/movein_2.txt'
# file = open(file_path, 'r')

# transcript = file.read()

# print(classify_call(transcript))




