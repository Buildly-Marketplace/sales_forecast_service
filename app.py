import numpy as np
from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
from flask_restplus import Api

app = Flask(__name__)
api = Api(app)

model = pickle.load(open('model.pkl', 'rb'))


@api.route('/dataset',methods=['GET'])
@api.doc()
def get_dataset():
    dataset = pd.read_csv('sales.csv').to_json()
    return jsonify(dataset)


@api.route('/results',methods=['POST'])
@api.doc()
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True,port=8000)
