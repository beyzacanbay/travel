import requests
import pprint
import json
city = input('City Name: ')
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=ded10e906df5e988adcdfcb5071da37b&units=metric'.format(city)



response = requests.get(url)
json_data = response.json()
main = json_data['main']
weather = json_data['weather'][0]

weather_condition=dict(list(main.items()) + list(weather.items()))
pprint.pprint(weather_condition)

#pprint.pprint(weather)


"""
print('Temperature : ', temp, chr(176), sep='')
print('Wind Speed : {}'.format(wind_speed),'m/s')
print('Latitude : {} '.format(latitude))
print('Longitude : {}'.format(longitude))
print('Description: {}'.format(description))

"""
