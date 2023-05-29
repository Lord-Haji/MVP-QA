import os
import openai

from config import API_KEY

openai.api_key = API_KEY



def extract_data(transcript):


    extract_prompt = """
    Name : 
    DOB : 
    Contact Number : 
    Email : 
    Postal Address : 
    Solar : 
    Delivery method : 
    Concession Card : 
    Issue Date :
    Expiry Date : 
    Secondary Account Holder Name : 
    Billing cycle offered : 
    Promotions mentioned : 
    Supply Address : 
    NMI : 
    MIRN : 

    [NOTE: If not confirmed then write - "NOT CONFIRMED"]

    [If agent did not capture from the customer's end then write - "NOT CAPTURED"]

    IF BUSINESS
    Business name / Account name :
    ABN :

    IF MOVE IN
    MOVE IN FEE :
    Date of move in/Connection :
    Power is currently Off/ On :
    Advised clear access for connection :

    Correct RATES advised to the customer :
    PLAN : 
    IVR : Yes
    Customer No : 
    RACT No : 
    VIC : 
    Current customer : No
    Did agent ask how customer heard about us : 
    Internet asked :
    """


    messages = [
        {
            "role": "system",
            "content": f"extract all this information mention below form the above transcript: '{transcript}'"
        },
        {"role": "user", "content": extract_prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        max_tokens=340,
    )

    return response["choices"][0]["message"]["content"].strip()

# Example usage
# file_path = 'transcripts/movein_2.txt'
# file = open(file_path, 'r')

# transcript = file.read()

# print(classify_call(transcript))




