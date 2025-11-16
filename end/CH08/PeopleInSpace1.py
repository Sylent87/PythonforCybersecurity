import requests
import json

url = "http://api.open-notify.org/astros.json"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)

astronauts = response.json()

#print(astronauts)
#print (json.dumps(astronauts, indent=2))
print ("There are {0} people in space right now." .format(astronauts["number"]))
print ("The first astronaut is {0}, aboard the {1}.".format(astronauts["people"][1]["name"], astronauts["people"[1]["craft"]]))
