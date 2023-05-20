import requests
import json
import pandas as pd

# Include your bitly access token here
ACCESS_TOKEN = ""

long_uri = input("Enter the long URL: ")

url = "https://api-ssl.bitly.com/v4/shorten"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}
data = {
    "long_url": long_uri
}

try:
    req = requests.post(url, headers=headers, data=json.dumps(data))
    res = req.json()
    print('\n', res['link'], '\n')

    with open('./data.json', 'r+') as file:
        f = list(pd.read_json('data.json'))
        f.append(json.dumps(res))
        file.write(json.dumps(f))
        file.close()

except ConnectionError as err:
    print(err)
