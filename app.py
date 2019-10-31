import numpy as np
from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/dataset',methods=['GET'])
def get_dataset():
    dataset = pd.read_csv('sales.csv').to_json()
    return jsonify(dataset)


@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True,port=8000)