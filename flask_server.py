
from flask import Flask, jsonify, request
from City import CityManager
from Region import RegionManager
from ThirdParty import WeatherCondition,Ticket

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def hello():
    return "Hello Time To Travel!"


@app.route("/places_to_visit/<string:city_name>")
def get_places_for_visit(city_name):
    cm = CityManager()
    result = cm.get_places_to_visit(city_name)
    return jsonify(result)


@app.route("/cities")
def get_cities():
    cm = CityManager()
    result = cm.get_all_cities()
    return jsonify(result)


@app.route("/region")
def get_regions():
    rm = RegionManager()
    result = rm.get_all_regions()
    return jsonify(result)


@app.route("/weathercondition/<string:city>")
def weather_condition(city):
    wc = WeatherCondition()
    weather_condition = wc.make_api_request(city)

    return weather_condition


@app.route("/ticket/query")
def ticket():
    dest_from_city = request.args.get('dest_from_city')
    dest_to_city = request.args.get('dest_to_city')
    date = request.args.get('date')
    ticket_control= Ticket()
    data = ticket_control.make_api_request(dest_from_city,dest_to_city,date)

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=1234)
