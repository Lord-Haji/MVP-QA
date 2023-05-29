import os
import openai
from config import API_KEY

openai.api_key = API_KEY

def generate_report(transcript, call_type):

    print(f"Classified as {call_type}")


    prompt_response = []

    # Define parameters for each call type
    parameters = {
        "inboundcancel": """
            - Greeting the customer: 15 points
            - Asking the customer's name, address, and date of birth: 30 points
            - Explaining the terms and conditions: 10 points
            - Informing the customer about rates and plans: 10 points
            - Inquiring about medical devices in the house: 15 points
            - Asking the customer's preference for receiving bills: 10 points
            - Asking about pets: 5 points
            - Asking about birds: 5 points
        """,
        "inboundmoveinsale": """
            Call Opening: 30 points
            ID Check: 30 points
            Clear Communication: 40 points
        """,
        # TODO: Parameters for rest of call types
    }

    # Retrieve parameters based on call type
    params = parameters.get(call_type, "")

    print(params)

    prompt = f"""
    Understand the call first. Based on the content and context of this conversation, which parameters were fulfilled? The parameters are:
    {params} Add the points assigned to each parameter fulfilled to the acquired points. If the acquired points is 80+ its a fail otherwise its a fail.
    Your output should be in format: [acquired points][pass or fail]
    """

    messages = [
        {
            "role": "system", 
            "content": f"Hello GPT, I have a call transcript that I would like you to analyze. Here is the transcript:'{transcript}'"
                        # f"{params} If the acquired score is 80+ and mandatory parameters pass, the transcript passes." +
                        # f"If it is below or any of the mandatory parameters fail, the transcript fails." +
                        # f"Summarize the review with a brief comment on the call in the end, And start with the points scored" 
        },
        {"role": "user", "content": f""}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        max_tokens=100,
    )

    return response["choices"][0]["message"]['content'].strip()

    # final_response = ""
    # for response in prompt_response:
    #     final_response += response

    # return final_response

# Example usage

# file_path = 'incoming.txt'
# file = open(file_path, 'r')

# transcript = file.read()

# call_type = "inboundcancel"

# report = generate_report(transcript, call_type)
# print(report)
