import requests
import json

url = "https://icanhazdadjoke.com/api"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
