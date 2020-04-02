import requests
import pprint

originCity=input("Enter your from city airport code:")
destCity=input("Enter dest to city airport code: ")
date=input("Enter time (YYYY-mm-dd): ")
url = "https://travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com/v2/prices/latest"

querystring = {"trip_class":"0","limit":"30","show_to_affiliates":"2","sorting":"price","one_way":"true","beginning_of_period":date,"currency":"TRY","page":"1","period_type":"day","origin":originCity,"destination":destCity}

headers = {
    'x-rapidapi-host': "travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com",
    'x-rapidapi-key': "d1da59d9f9mshfa683ef9c6fda8ep1e59bcjsnd1580194e65d",
    'x-access-token': "d04ac8b64635eee36d3cbfd230460faf"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


json_data = response.json()
pprint.pprint(json_data)

