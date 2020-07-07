from datetime import datetime
from datetime import timedelta
import json
from flask_cors import CORS
from flask import Flask, request
from predict import predict_weather1, RetValEncoder
import pandas as pd
from waitress import serve

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['GET', 'POST'])
def predict_weather():
    day = int(request.args.get('day'))
    month = int(request.args.get('mon'))
    year = int(request.args.get('year'))
    total_days = int(request.args.get('numdays'))
    date_start = datetime.today()
    print(date_start)
    predicted = predict_weather1(year, month, day, total_days)
    jsons = RetValEncoder().encode(predicted)
    return jsons


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5001)
