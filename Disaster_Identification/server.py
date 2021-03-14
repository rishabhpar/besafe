# Import libraries
import numpy as np
from flask import Flask, request, jsonify
import pickle
import pandas as pd 
from ernie import SentenceClassifier, Models, AggregationStrategies
from commonregex import CommonRegex
import googlemaps

app = Flask(__name__)

# Load the model
classifier = SentenceClassifier(model_path='./model')
gmaps = googlemaps.Client(key='AIzaSyAKLe-3vkSSHZ67pkBrxEjCnZDffKOUXNU')


@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    df = pd.DataFrame([data['text']], columns=['text'])
    
    probabilities = classifier.predict(df['text'],
                                    aggregation_strategy=AggregationStrategies.Mean)
    predictions = list(n for n in probabilities)

    label = None
    if predictions[0][0] > predictions[0][1]:
        label = 'unsafe'
    else:
        label = 'safe'

    addy = CommonRegex(data['text']).street_addresses

    if addy:
        geocode_result = gmaps.geocode(addy)
        coordinates = geocode_result[0]['geometry']['location']
        # print(str(coordinates['lat']) + ", " + str(coordinates['lng']))

    loc = None
    if addy:
        loc = str(coordinates['lat']) + ", " + str(coordinates['lng'])
    else: 
        loc = 'null'


    # Make prediction using model loaded from disk as per the data.
    # Take the first value of prediction
    return jsonify(text=data['text'],
                   label=label,
                   location=loc)


if __name__ == '__main__':
    app.run(port=5000, debug=False)