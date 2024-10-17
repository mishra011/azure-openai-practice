import os
import requests
import base64

# Configuration
API_KEY = "xxxxxxxxxxxxx"
IMAGE_PATH = "statue-of-unity.jpg"
encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
}

# Payload for the request
payload = {
  "messages": [
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "You are an AI assistant that helps people find information."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "\n"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{encoded_image}"
          }
        },
        {
          "type": "text",
          "text": "Summarize the image and make sure to preserve the meaning"
        }
      ]
    }
  ],
  "temperature": 0.7,
  "top_p": 0.95,
  "max_tokens": 800
}

ENDPOINT = "https://openaixxxxxx.openai.azure.com/openai/deployments/xxxxxx/chat/completions?api-version=2024-02-15-xxxxxx"

# Send request
try:
    response = requests.post(ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
except requests.RequestException as e:
    raise SystemExit(f"Failed to make the request. Error: {e}")

# Handle the response as needed (e.g., print or process)
print(response.json())