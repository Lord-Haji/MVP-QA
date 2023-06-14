import os
from dotenv import load_dotenv, find_dotenv

# Check if a .env file exists
def load_environment_variables():
    if os.path.exists('.env'):
        load_dotenv(find_dotenv())

load_environment_variables()

API_KEY = os.getenv("OPENAIAPI_KEY")

DATABASE_FILE = 'transcriptions.db'