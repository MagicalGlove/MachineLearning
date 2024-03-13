from flask import Flask, jsonify, request
from joblib import  load
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    model = load('RandomForest.joblib')
    array = request.json
    print(array)
    data = pd.Series(array)
    data['volume']=data['x'];data['y'];data['z']
    data=data.drop(['x','y','z'])
    new_cut = {'Fair':1,'Good':2,'Very Good':3, 'Premium':4,'Ideal':5}
    data['cut'] = new_cut.get(data['cut'], 3)
    new_color = {'J':1,'I':2, 'H':3,'G':4,'F':5,'E':6,'D':7}
    data['color'] = new_color.get(data['color'], 4)
    new_clarity = {'I1':1,'SI2':2,'SI1':3,'VS2':4,'VS1':5,'VVS2':6,'VVS1':7,'IF':8}
    data['clarity'] = new_clarity.get(data['clarity'], 4)
    converted_data = np.array(data).reshape(1, -1)
    model_result = model.predict(converted_data).tolist()
    prediction = {'result': model_result}
    print('model prediction:', prediction)

    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True)