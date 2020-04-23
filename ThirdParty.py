from abc import ABC, abstractmethod
import requests

class ThirdParty(ABC):

    @abstractmethod
    def make_api_request(self,*args,**kwargs):
        pass

class WeatherCondition(ThirdParty):
    def make_api_request(self,*args,**kwargs):
        city = args[0]

        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=ded10e906df5e988adcdfcb5071da37b&units=metric'.format(
            city)
        response = requests.get(url)
        json_data = response.json()
        main = json_data['main']
        weather = json_data['weather'][0]
        weather_condition = dict(list(main.items()) + list(weather.items()))
        return weather_condition

class Ticket(ThirdParty):
    def make_api_request(self,*args,**kwargs):
        dest_from_city = args[0]
        dest_to_city=args[1]
        date=args[2]
        url = "https://travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com/v2/prices/latest".format(
            dest_from_city, dest_to_city, date)

        querystring = {"trip_class": "0", "limit": "30", "show_to_affiliates": "2", "sorting": "price",
                       "one_way": "true",
                       "beginning_of_period": date, "currency": "TRY", "page": "1", "period_type": "day",
                       "origin": dest_from_city, "destination": dest_to_city}

        headers = {
            'x-rapidapi-host': "travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com",
            'x-rapidapi-key': "d1da59d9f9mshfa683ef9c6fda8ep1e59bcjsnd1580194e65d",
            'x-access-token': "d04ac8b64635eee36d3cbfd230460faf"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        json_data = response.json()