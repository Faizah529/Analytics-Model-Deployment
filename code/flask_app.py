
# A very simple Flask Hello World app for you to get started with...

#from flask import Flask

#app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello from Flask!'


# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
from flask import Flask, request, jsonify
from sklearn.externals import joblib
import numpy as np

app = Flask(__name__)

# Load the model
model = joblib.load('/home/Faizah/mysite/Credit Scoring using Random Forest.pkl')

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    datas = request.get_json(force=True)

    pred=[]

    for data in datas:
        # Make prediction using model loaded from disk as per the data.
        prediction = model.predict([np.array([data['LIMIT_BAL'],data['AGE'], data['BILL_AMT1'], data['BILL_AMT2'], data['BILL_AMT3'], data['PAY_AMT1'],
            data['PAY_AMT2'], data['PAY_AMT3'], data['MARRIAGE_1'], data['MARRIAGE_2'], data['MARRIAGE_3'],
            data['EDUCATION_1'], data['EDUCATION_2'], data['EDUCATION_3'], data['EDUCATION_4'], data['SEX_1'],
            data['SEX_2'], data['PAY_1_0'], data['PAY_1_1'], data['PAY_1_2'], data['PAY_1_3'], data['PAY_1_4'],
            data['PAY_2_0'], data['PAY_2_1'], data['PAY_2_2'], data['PAY_2_3'], data['PAY_2_4'], data['PAY_3_0'],
            data['PAY_3_1'], data['PAY_3_2'], data['PAY_3_3'], data['PAY_3_4']])])

        # Take the first value of prediction
        output = float(prediction[0])
        out='Pass' if output==1 else 'Tidak Terlambat'
        pred.append(out)

    return jsonify(pred)