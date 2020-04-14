import sqlite3
from flask import Flask, jsonify, request
import requests
import pprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False



@app.route("/")
def hello():
    return "Hello Time To Travel!"
@app.route("/cities")
def add_city():
    con = sqlite3.connect("database.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM places")
    rows = cursor.fetchall()
    result = []
    for item in rows:
        if not None in item:
            result.append({"Id": item[0], "city_name": item[1],"region": item[2], "description": item[3],"lat": item[4], "lon": item[5]})
        print(item)

    con.commit()
    con.close()
    return jsonify(result)
@app.route("/weathercondition/<string:city>")
def weather_condition(city):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=ded10e906df5e988adcdfcb5071da37b&units=metric'.format(city)
    response = requests.get(url)
    json_data = response.json()
    main = json_data['main']
    weather = json_data['weather'][0]
    weather_condition = dict(list(main.items()) + list(weather.items()))

    return weather_condition

    
@app.route("/region")
def get_region():
    con = sqlite3.connect("database.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM region")
    rows = cursor.fetchall()
    result = []
    for item in rows:
        result.append({"Id": item[0], "region_name": item[1], "photo": item[2]})
    con.commit()
    con.close()


    return jsonify(result)

    
@app.route("/ticket/query")
def ticket():



    dest_from_city = request.args.get('dest_from_city')
    dest_to_city = request.args.get('dest_to_city')
    date = request.args.get('date')
    url = "https://travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com/v2/prices/latest".format(
        dest_from_city, dest_to_city, date)

    querystring = {"trip_class": "0", "limit": "30", "show_to_affiliates": "2", "sorting": "price", "one_way": "true",
                   "beginning_of_period": date, "currency": "TRY", "page": "1", "period_type": "day",
                   "origin": dest_from_city, "destination": dest_to_city}

    headers = {
        'x-rapidapi-host': "travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com",
        'x-rapidapi-key': "d1da59d9f9mshfa683ef9c6fda8ep1e59bcjsnd1580194e65d",
        'x-access-token': "d04ac8b64635eee36d3cbfd230460faf"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    json_data = response.json()
    return jsonify(json_data)

if __name__ == '__main__':

    app.run(debug=True, host="0.0.0.0", port=1234)