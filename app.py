from flask import Flask, request, render_template, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from datetime import timedelta
import joblib
import numpy as np

app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30) #Session limited to 30 minutes
limiter = Limiter(key_func=get_remote_address, app=app) #Rate limiter to prevent DDOS attacks

model = joblib.load('models/trained_model.pkl') #Load trained model and get unique values for target audience and channel used

@app.route ('/')
def index():
    return render_template('index.html')

@limiter.limit("15 per minute") #Limited to 15 requests per minute
@app.route ('/predict', methods=['POST'])
def predict():
    #Fetch input values for the features from website
    target_audience = request.form.get('target_audience')
    channel_used = request.form.get('channel_used')

    try:
        target_audience = int(target_audience)
        channel_used = int(channel_used)
        if target_audience < 0 or channel_used < 0:  # Input Validation
            raise ValueError
    except (ValueError, TypeError):
        abort(400)  # Bad request

    #Prepare input data to send to model for prediction
    features = np.array ([[target_audience, channel_used]])
    prediction = model.predict(features)

    return render_template('result.html', prediction = prediction)

#Handle any errors, redirect to different page
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=False)