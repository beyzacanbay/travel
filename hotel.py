import requests
import pprint
url = "https://hotels4.p.rapidapi.com/locations/search"

querystring = {"locale":"en_US","query":"istanbul"}

headers = {
    'x-rapidapi-host': "hotels4.p.rapidapi.com",
    'x-rapidapi-key': "d1da59d9f9mshfa683ef9c6fda8ep1e59bcjsnd1580194e65d"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
json_data = response.json()
pprint.pprint(json_data)