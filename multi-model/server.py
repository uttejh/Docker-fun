#import pickle
from flask import Flask, request, jsonify
#import pandas as pd
#import numpy as np

# app = Flask(__name__)
#
# @app.route("/")
# def fello():
#     print("hello")
#
#
# # @app.route("/api", methods=["POST"])
# # def predict():
# #     filename = "model/model.sav"
# #     model = pickle.load(open(filename, 'rb'))
# #
# #     data = request.get_json()
# #     data = pd.DataFrame(data["data"]).T
# #
# #     prediction = np.array2string(model.predict(data))
# #
# #     return jsonify(prediction)
#
#
# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0")

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
