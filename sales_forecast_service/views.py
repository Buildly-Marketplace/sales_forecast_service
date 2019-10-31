import pandas as pd
import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
file = open('sales_forecast_service/models/model.pkl', 'rb')
model = pickle.load(file)

@app.route('/dataset',methods=['GET'])
def get_dataset():
    dataset = pd.read_csv('sales_forecast_service/datasets/sales.csv').to_json()
    return jsonify(dataset)


@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)