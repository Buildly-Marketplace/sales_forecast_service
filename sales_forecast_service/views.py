import pandas as pd
import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
model = pickle.load(open('models/model.pkl', 'rb'))

@app.route('/dataset',methods=['GET'])
def get_dataset():
    dataset = pd.read_csv('datasets/sales.csv').to_json()
    return jsonify(dataset)


@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)