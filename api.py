import flask
import json
import numpy as np
from sklearn.externals import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return flask.render_template('index.html')

@app.route("/predict", methods=['POST'])
def make_predictions():
        if request.method =='POST':
                sl = request.form.get('sepal-length')
                sw = request.form.get('sepal-width')
                pl = request.form.get('petal-length')
                pw = request.form.get('petal-width')
                X = np.array([sl,sw,pl,pw]).reshape(1,-1)
                prediction = model.predict(X)
                resultText = json.dumps(prediction.tolist(),sort_keys = False)
                # This json.dumps will convert 'prediction' to JSON
                return render_template('predictPage.html',response=resultText)
                # 'response' is a Jinja2 variable embedded in predictPage.html

# if __name__ == '__main__':
model = joblib.load('model.pkl')
    # app.run(host='0.0.0.0', port=8000, debug=True)
