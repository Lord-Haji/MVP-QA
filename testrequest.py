import requests

url = "http://127.0.0.1:8000/transcribe_audio"

headers = {
    "accept": "application/json",
}

filepath = "audio/cancel_1.mp3"

with open(filepath, 'rb') as f:
    files = {
        'audio_file': (filepath, f, 'audio/mpeg'),
    }
    response = requests.post(url, headers=headers, files=files)

# The response from the server
print(response.json())
