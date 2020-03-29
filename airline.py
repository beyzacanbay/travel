import requests

params = {
  'access_key': '121b145a559356b7dddb9045c154b73c'
}
print(params)

api_result = requests.get('https://api.aviationstack.com/v1/flights', params)

api_response = api_result.json()

print(api_response)