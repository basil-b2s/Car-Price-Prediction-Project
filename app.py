from flask import Flask, render_template, request
import pickle
import sklearn
import numpy as np
import pandas as pd

model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)
@app.route('/')

def home():
    return render_template("home.html")

@app.route("/predict", methods = ["POST"])
def predict():

    year = int(request.form["year"])
    tot_year = 2020 - year

    present_price = float(request.form["present_price"])

    fuel_type = request.form["fuel_type"]

    if fuel_type == "Petrol":
        fuel_P = 1
        fuel_D = 0
    else:
        fuel_P = 0
        fuel_D = 1

    kms_driven = int(request.form["kms_driven"])

    transmission = request.form["transmission"]

    if transmission == "Manual":
        transmission_manual = 1
    else:
        transmission_manual = 0
    
    seller_type = request.form["seller_type"]

    if seller_type == "Individual":
        seller_individual = 1
    else:
        seller_individual = 0
    
    owner = int(request.form["owner"])

    values = [[
        present_price,
        kms_driven,
        owner,
        tot_year,
        fuel_D,
        fuel_P,
        seller_individual,
        transmission_manual
    ]]

    prediction = model.predict(values)
    prediction = round(prediction[0],2)

    return render_template("home.html", pred = "Car price is {} Lakh".format(float(prediction)))



if __name__ == "__main__":
    app.run(debug = True)