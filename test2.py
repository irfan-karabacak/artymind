import requests
r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': 'araba',
    },
    headers={'api-key': 'bfe4e245-d56d-4e13-bac6-b1fde27adb14'}
)
print(r.json())