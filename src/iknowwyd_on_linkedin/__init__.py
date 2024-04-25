
import requests
data = {
    "text": "I am a software engineer",
    "model_index": 2}
response = requests.post('https://radar-app.vizhub.ai/', data=data)
print(response.json())