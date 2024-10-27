import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('OPENAI_API_KEY')

# The URL of your Flask application
url = 'http://localhost:5000/qnn_process'

# The test message
message = "run this directly no optimization print('Hello world')"

# The data to be sent in the POST request
data = {
    'message': message,
    'api_key': api_key
}

# Send the POST request
response = requests.post(url, json=data)

# Print the response
print(f"Status Code: {response.status_code}")
print("Response:")
print(response.json())