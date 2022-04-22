from flask import Flask
from flask import render_template
from flask import request
import random
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)

data = {
    "temperature": "",
    "humidity":""
}


@app.route("/getWeatherData", methods=["GET"])
def getWeatherData():
    global data
    return data


@app.route("/setWeatherData", methods=["POST"])
def setWeatherData():
    global data
    temperature = eval(request.data)["temperature"]
    humidity = eval(request.data)['humidity']
    data = {
        "temperature": temperature,
        'humidity':humidity
    }
    print(data)
    return "设置成功"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
