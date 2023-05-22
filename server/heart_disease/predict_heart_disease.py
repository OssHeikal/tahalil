import numpy as np
import pickle

import pandas as pd
from flask import jsonify, render_template
from utils.helpers.messages import Messages


def heartpd(ST_Slope_Up, Oldpeak, Cholesterol, ExerciseAngina_Y, MaxHR, Sex_M, Age, RestingBP):
    classes = ["Negative", "Positive"]
    features = [[ST_Slope_Up, Oldpeak, Cholesterol, ExerciseAngina_Y, MaxHR, Sex_M, Age, RestingBP]]
    input_array = np.array(features)
    model = pickle.load(open("server/heart_disease/heart_model.pkl", "rb"))
    pred = model.predict(input_array)
    class_pred = classes[pred[0]]
    return class_pred

def predict_heart_disease(data):
    # Get the input data from the request
    ST_Slope_Up = int(data["ST_Slope_Up"])
    Oldpeak = float(data["Oldpeak"])
    Cholesterol = int(data["Cholesterol"])
    ExerciseAngina_Y = int(data["ExerciseAngina_Y"])
    MaxHR = int(data["MaxHR"])
    Sex_M = int(data["Sex_M"])
    Age = int(data["Age"])
    RestingBP = int(data["RestingBP"])
    result = heartpd(ST_Slope_Up, Oldpeak, Cholesterol, ExerciseAngina_Y, MaxHR, Sex_M, Age, RestingBP)
    return result

def send_herat_json(result, data):
    report = Messages.heart_disease_message(result,data['ST_Slope_Up'], data['Oldpeak'],data['Cholesterol'] ,data['ExerciseAngina_Y'], data['MaxHR'], data['Sex_M'], data['Age'], data['RestingBP'] )
    return jsonify({
        "status": "success",
        "prediction": result,
        "report":report
    })
def render_heart_result(result, report):
    return render_template("result_heart.html", prediction=result, report=report)