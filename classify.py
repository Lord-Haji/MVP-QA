import os
import openai

from config import API_KEY

openai.api_key = API_KEY



def classify_audio(transcript):


    classify_prompt = """
    The list of categories and subcategories along with an explanation of when which is appropriate are described in the text delimeted by triple backticks \
    the categories are listed below along with the possible subcateogires belonging to a category are delimeted with #### and listed
    ```
    Inbound: (customer initiated)
    ####
    - Cancel: (expressing dissatisfaction and intent to cancel service and canceled service in the end)
    - Transfer Sale: (discussing transferring their service from an existing provider to us)
    - Move-in Sale: (discussing setting up service at a new location)
    - Retention: (existing first-energy customer, discussing potential cancellation but can be persuaded to stay and didn't cancel in the end)
    - SMS Sale: (customer was served or sent an SMS or text message any time throughout the duration of the transcript)
    ####
    Outbound: (company initiated)
    ####
    - Transfer: (discussing transferring customer's service from an existing provider to us)
    - Move-in: (discussing setting up service at a new location for the customer)
    - Retention: (outreach to customers at risk of cancelling service)
    - SMS Sale: (promoting or selling services via SMS)
    ####
    Channel: (initiated by partner agency)
    ####
    - Transfer: (discussing transferring customer's service from an existing provider to us)
    - Move-in: (discussing setting up service at a new location for the customer)
    ####
    Credit: (discussing credit-related or transaction issues)
    ####
    - Quality Assurance: (focused on quality assurance)
    - VIC PDF: (specific to Victoria region, discussing issues about payment difficulty, call is handeled by credit team: Hoang Le, Kate Williams, Rabia Sheikh, Pooja Dhir, Garima Dembla, Shruthi Selvakumar, Isaac Kim, Rose Simpson)
    - Customer Support VIC PDF: (specific to Victoria region, discussing issues about payment difficulty)
    ####
    
    The steps you should follow to analyze the call are as follows
    Step 1: Classify the transcript into one of the following categories
    Step 2: Classify the transcript into one of the subcategories belonging to the identified category

    Your Output should be a JSON object with the keys being category , subcategory and reason and the values being the classified category and subcategory string converted into all lowercase without special characters and reason should be your reasoning for picking the specific category and subcategory
    """


    messages = [
        {
            "role": "system",
            "content": f"Hello GPT, I have a call transcript that I'd like you to classify. Here is the transcript: '{transcript}'"
        },
        {"role": "user", "content": classify_prompt},

    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
        temperature=0,
        max_tokens=100,
    )

    return response["choices"][0]["message"]["content"].strip()

# Example usage
# file_path = "movein_2.txt"
# classification = classify_call(file_path)
# print(classification)

# print(count_tokens(file_path))

