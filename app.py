""" Code Challenge from ENGIE_GEM_SPaaS and TMC """
from operator import itemgetter
from flask import Flask, jsonify, app, request, abort

app = Flask(__name__)

def read_json(key,json):
    """ Search the json key in content, content is a json file """
    if key in json:
        result = json[key]
        app.logger.info(key,' found: ',result,' - OK')
    else:
        app.logger.info(key,'NOT found')
        abort(400)
    return result

@app.route('/productionplan', methods=['GET', 'POST'])
def producionplan():
    """ This is the main function that calculates the 
    load each powerplant shoul give to achieve 
    the required load by network"""

    # get data!
    load = read_json("load",request.json)
    powerplants = read_json("powerplants",request.json)
    fuels = read_json("fuels",request.json)

    # sort data and initialize!
    powerplants_efficiency = sorted(powerplants, key=itemgetter('efficiency'), reverse=True)
    powerplants_p = {}
    powerplants_p = powerplants_efficiency
    res_load = load
    sum_p = 0

    # Calculate load available from each plant
    for powerplant in powerplants_efficiency:
        if powerplant["type"] == "windturbine":
            powerplant["p"] = powerplant["pmax"]* fuels["wind(%)"] / 100
        elif powerplant["type"] == "gasfired":
            powerplant["p"] = powerplant["pmax"]* fuels["wind(%)"] / 100
        elif powerplant["type"] == "turbojet":
            powerplant["p"] = powerplant["pmax"]* fuels["wind(%)"] / 100

    # Search which plant gives less thann 100%
    for powerplant in powerplants_efficiency:
        res_load -= powerplant["p"]
        if res_load < 0:
            powerplant["p"] = 0

    # Calculte load of the plant wich is not at 100%
    for powerplant in powerplants_efficiency:
        sum_p += powerplant["p"]
        if powerplant["p"] == 0:
            powerplant["p"] = load - sum_p
            break

    # delete extra data from dictionary
    for powerplant in powerplants_p:
        del powerplant["type"]
        del powerplant["efficiency"]
        del powerplant["pmin"]
        del powerplant["pmax"]

    return jsonify(powerplants_efficiency)

if __name__ == "__main__":
    app.run(debug=False)
    app.run(host='localhost')
