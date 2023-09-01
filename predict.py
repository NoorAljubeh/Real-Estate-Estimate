from flask import Flask, render_template, request, jsonify, redirect, url_for
import pandas as pd
from joblib import load

app = Flask(__name__)

features_order = [
    "longitude",
    "latitude",
    "housing_median_age",
    "total_rooms",
    "total_bedrooms",
    "population",
    "households",
    "median_income",
    "<1H OCEAN",
    "INLAND",
    "ISLAND",
    "NEAR BAY",
    "NEAR OCEAN",
]


@app.route("/", methods=["GET", "POST"])
def home_page():
    return render_template("./index.html")


@app.route("/predict_price", methods=["GET", "POST"])
def predict_price():
    try:
        data = request.get_json(force=True)
        model = load("./static/model.joblib")
        house_info = sort_data_based_on_features_order(data)
        print(house_info)
        price_prediction = model.predict(pd.DataFrame.from_dict([house_info]))[0].item()

        return jsonify(
            message="Success",
            value=price_prediction,
            status=200,
            mimetype="application/json",
        )

    except Exception as err:
        print(err)
        return jsonify(message="ERROR", status=405, mimetype="application/json")

    return "null"


def sort_data_based_on_features_order(data):
    element_to_position = {
        element: position for position, element in enumerate(features_order)
    }

    # Sort the second list based on the positions in the first list
    ordered_features = sorted(
        data.keys(), key=lambda element: element_to_position[element]
    )
    ordered_features_dict = {key: data[key] for key in ordered_features}

    return ordered_features_dict


if __name__ == "__main__":
    app.run(debug=True)
