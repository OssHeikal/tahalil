import numpy as np
import pickle

import pandas as pd
from flask import jsonify, render_template
from utils.helpers.messages import Messages

def diabetes_X(age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level, smoking_history_current, smoking_history_former, gender_Male):
    classes = ["Negative", "Positive"]
    input_array = np.array([[age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level, smoking_history_current, smoking_history_former, gender_Male]])
    d_model = pickle.load(open("server/diabetes/diabetes_XGB.pkl", "rb"))
    pred = d_model.predict(input_array)
    class_pred = classes[pred[0]]
    return class_pred

def predict_diabetes(data):
    age = int(data["age"])
    hypertension = int(data["hypertension"])
    heart_disease = int(data["heart_disease"])
    bmi = float(data["bmi"])
    HbA1c_level = float(data["HbA1c_level"])
    blood_glucose_level = float(data["blood_glucose_level"])
    smoking_history_current = int(data["smoking_history_current"])
    smoking_history_former = int(data["smoking_history_former"])
    gender_Male = int(data["gender"])
    result = diabetes_X(age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level, smoking_history_current, smoking_history_former, gender_Male)
    
    return result

def send_diabetes_json(result, data):
    report = Messages.diabetes_message(data['age'], data['hypertension'], data['heart_disease'], data['bmi'], data['HbA1c_level'], data['blood_glucose_level'], data['smoking_history_current'], data['smoking_history_former'], data['gender'], result)
    return jsonify({
        "status": "success",
        "prediction": result,
        "report": report
    })

def render_diabetes_result(result, report):
    return render_template("result_diabetes.html", prediction=result, report=report)