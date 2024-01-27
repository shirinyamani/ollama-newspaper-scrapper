import json

import requests


def translate_and_summary(model, prompt, stream=False):
    url = "http://localhost:11434/api/generate"
    data = {
        'model' : model,
        'prompt' : prompt,
        'stream' : stream
    }
    json_data = json.dumps(data)
    response = requests.post(url, json_data, headers={'Content-Type': 'application/json'})
    if response.status_code == 200:
        print(response.json()['response'])
    
    return f'Error code is: {response.status_code}'