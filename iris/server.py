from flask import Flask, request, jsonify
from sklearn.externals import joblib
import pandas as pd

app = Flask(__name__)


@app.route("/")
def fello():
    return "hello"


@app.route("/api", methods=["POST"])
def predict():
    filename = "model/model.sav"
    model = joblib.load(filename)

    data = request.get_json()
    data = pd.DataFrame(data, index=[0]).T
    input = [data[0]]

    target_names = ['setosa', 'versicolor', 'virginica']

    prediction = model.predict(input)
    return jsonify(target_names[prediction[0]])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
