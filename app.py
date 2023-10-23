""" DocString """
import os
from operator import itemgetter
from flask import Flask, jsonify, app, request

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['TESTING'] = False

def read_json(key,json):
    """ search the json key in content, content is a json file """
    if key in json:
        result = json[key]
        print(key,' found: ',result,' - OK ')
    return result

@app.route('/productionplan', methods=['GET', 'POST'])
def producionplan():
    """ Docstring"""
    load = read_json("load",request.json)
    powerplants = read_json("powerplants",request.json)
    fuels = read_json("fuels",request.json)
    powerplants_efficiency = sorted(powerplants, key=itemgetter('efficiency'), reverse=True)
    powerplants_p = {}

    result = 0
    for powerplant in powerplants_efficiency:
        if powerplant["type"] == "windturbine":
            powerplant["p"] = powerplant["pmax"]* fuels["wind(%)"] / 100
        elif powerplant["type"] == "gasfired":
            powerplant["p"] = powerplant["pmax"]* fuels["wind(%)"] / 100
        elif powerplant["type"] == "turbojet":
            powerplant["p"] = powerplant["pmax"]* fuels["wind(%)"] / 100

    for powerplant in powerplants_efficiency:
        if load - result <= 0:
            break
        result += powerplant["p"]
        print(result)
    if result < load:
        print("NOT enough power!")

    powerplants_p = powerplants_efficiency
    for powerplant in powerplants_p:
        del powerplant["type"]
        del powerplant["efficiency"]
        del powerplant["pmin"]
        del powerplant["pmax"]

    return jsonify(powerplants_efficiency)

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='localhost')
