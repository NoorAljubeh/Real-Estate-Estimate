from flask import Flask, render_template, request, jsonify, redirect, url_for
import pandas as pd
from joblib import load

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home_page():
    return render_template("./index.html")


@app.route("/predict_price", methods=["GET", "POST"])
def predict_price():
    try:
        data = request.get_json(force=True)
        model = load("./static/model.joblib")
        price_prediction = model.predict(pd.DataFrame.from_dict([data]))[0].item()
        return jsonify(
            message="Success",
            value=price_prediction,
            status=200,
            mimetype="application/json",
        )

    except Exception as err:
        print(err, "AAAAAAAAAAAAAAA")
        return jsonify(message="ERROR", status=405, mimetype="application/json")

    return "null"


if __name__ == "__main__":
    app.run(debug=True)
