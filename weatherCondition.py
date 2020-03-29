import requests
import pprint
import pandas as pd
import json
city = input('City Name: ')
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=ded10e906df5e988adcdfcb5071da37b&units=metric'.format(city)


response = requests.get(url)
json_data = response.json()
json_data_coord = json_data['coord']
#pprint.pprint(json_data)
#print(type(json_data))

#temp = json_data['main']
#feels = json_data['main']['feels_like']
#wind_speed = json_data['wind']['speed']
#temp_min = json_data['main']['temp_min']
#temp_max = json_data['main']['temp_max']
#description = json_data['weather'][0]['description']
pprint.pprint(json_data)


"""
print('Temperature : ', temp, chr(176), sep='')
print('Wind Speed : {}'.format(wind_speed),'m/s')
print('Latitude : {} '.format(latitude))
print('Longitude : {}'.format(longitude))
print('Description: {}'.format(description))


with open('json_data.txt', 'w') as json_file:
  json.dump(json_data, json_file)
"""
