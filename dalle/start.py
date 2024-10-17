import os
import openai
from PIL import Image
from io import BytesIO
import requests

# Set up your Azure OpenAI API credentials
openai.api_key = "YOUR_AZURE_OPENAI_API_KEY"
openai.api_type = "azure"
openai.api_base = "https://YOUR_AZURE_OPENAI_ENDPOINT.openai.azure.com/"
openai.api_version = "2023-06-01-preview"  # Use the correct version for your instance

# Define the DALL-E prompt and parameters
prompt = "a futuristic cityscape with flying cars and neon lights"

response = openai.Image.create(
    prompt=prompt,
    n=1,  # Number of images to generate
    size="1024x1024"  # Image resolution
)

# Get the URL of the generated image
image_url = response['data'][0]['url']

# Download and display the image
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# Display the image
image.show()

# Optional: Save the image locally
image.save("generated_image.png")

