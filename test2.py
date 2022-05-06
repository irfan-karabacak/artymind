import requests

headers = {
    "Authorization": "API_KEY_HERE",
}

# change to a full file path of the image you want to transform
body = {
    "image": open("/full/path/to/image.jpg", "rb"),
}

response = requests.post(
    "https://api.hotpot.ai/remove-background", headers=headers, files=body
)

# change to a full file path where you want to save the resulting image
with open("/full/path/to/image-nobg.jpg", "wb") as file:
    file.write(response.content)
