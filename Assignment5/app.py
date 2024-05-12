from flask import Flask, jsonify, request
from joblib import  load
import numpy as np
import pandas as pd
from Model import vector_search

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def predict():
    req = request.json
    query = req["query"]
    print(query)
    db_response = vector_search(query)
    

    return jsonify('')

if __name__ == '__main__':
    app.run(debug=True)