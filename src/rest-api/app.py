import json

from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'OK!'


@app.route('/forecast', methods=['GET'])
def forecast():
    # payload = json.loads(request.data)

    # TODO: dynamically predict values
    # Load CSV
    # Prepare model
    # Predict values with model
    # Export values to JSON

    # Dummy data: generate series from start of 2016 to end of 2020
    series = pd.date_range(start='2016-01-01', end='2020-12-31', freq='D')

    return json.dumps(series, indent=4, sort_keys=True, default=str)


if __name__ == '__main__':
    app.run()
