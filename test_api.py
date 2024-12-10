import requests

# API endpoint
url = "http://127.0.0.1:5000/generate"

# Data to send to the API
data = {"prompt": "A futuristic city at night"}

# Make the POST request
response = requests.post(url, json=data)

# Print the response
print("Response status code:", response.status_code)
print("Response data:", response.json())
