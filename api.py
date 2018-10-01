import flask
import numpy as np
from scipy import misc
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
                # X =[[float(X['sepalLength']), float(X['sepalWidth']), float(X['petalLength']), float(X['petalWidth'])]]
                prediction = model.predict(X)
                response = {}
                response['predictions'] = prediction

                return flask.jsonify(prediction.tolist())


if __name__ == '__main__':
    model = joblib.load('model.pkl')
    app.run(host='0.0.0.0', port=8000, debug=True)
