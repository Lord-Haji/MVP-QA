import json

# Open the file
with open('parameters.json', 'r') as f:
    # Load the JSON data from the file
    data = json.load(f)

# Now the JSON data is stored as a Python dictionary in the `data` variable
print(data["inbound"]["transfersale"]["check_list"])
