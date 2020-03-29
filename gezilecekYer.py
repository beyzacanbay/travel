import requests
import pprint
url = "https://spott.p.rapidapi.com/places"

querystring = {"type":"CITY","limit":"10","language":"en","skip":"0","country":"TR","q":"ankara"}

headers = {
    'x-rapidapi-host': "spott.p.rapidapi.com",
    'x-rapidapi-key': "d1da59d9f9mshfa683ef9c6fda8ep1e59bcjsnd1580194e65d"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
json_data = response.json()
pprint.pprint(json_data)