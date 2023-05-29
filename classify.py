import os
import openai

from config import API_KEY

openai.api_key = API_KEY



def classify_call(transcript):


    classify_prompt = """
    Understand the call first. Based on the content and context of this conversation, which category and subcategory does it belong to? The options are:
    Inbound:
    - Cancel (customer initiated, expressing dissatisfaction and intent to cancel service and canceled service in the end)
    - Transfer Sale (customer initiated, discussing transferring their service from an existing provider to us)
    - Move-in Sale (customer initiated, discussing setting up service at a new location)
    - Retention (customer initiated, existing first-energy customer, discussing potential cancellation but can be persuaded to stay and didn't cancel in the end)
    - SMS Sale (customer initiated, discussing purchase or changes to service via SMS, customer was sucessfully served via a text message)
    Outbound:
    - Transfer (company initiated, discussing transferring customer's service from an existing provider to us)
    - Move-in (company initiated, discussing setting up service at a new location for the customer)
    - Retention (company initiated, outreach to customers at risk of cancelling service)
    - SMS Sale (company initiated, promoting or selling services via SMS)
    Channel Partner:
    - Transfer (initiated by a partner agency, discussing transferring customer's service from an existing provider to us)
    - Move-in (initiated by a partner agency, discussing setting up service at a new location for the customer)
    Credit Calls:
    - Credit Quality Assurance (discussing credit-related issues, focused on quality assurance)
    - Victoria PDF (specific to Victoria region, discussing credit-related issues via PDF)
    - Customer Support VIC PDF (specific to Victoria region, discussing general customer support issues via PDF)
    Your Output should be in format [category]:[subcategory]
    """


    messages = [
        {
            "role": "system",
            "content": f"Hello GPT, I have a call transcript that I'd like you to classify. Here is the transcript: '{transcript}'"
        },
        {"role": "user", "content": classify_prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        max_tokens=28,
    )

    return response["choices"][0]["message"]["content"].strip()

# Example usage
# file_path = "movein_2.txt"
# classification = classify_call(file_path)
# print(classification)

# print(count_tokens(file_path))

