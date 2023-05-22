import numpy as np
import pickle

from flask import jsonify, render_template

from utils.helpers.messages import Messages

def anemiadet(gender, hgb):
    classes = ["Negative", "Positive"]
    input_array = np.array([[gender, hgb]])
    model1 = pickle.load(open("server/anemia/anemia_model.pkl", "rb"))
    pred = model1.predict(input_array)
    class_pred = classes[pred[0]]
    return class_pred

def predict_anemia(data):
    gender = int(data["gender"])
    hemoglobin = float(data["hemoglobin"])
    result = anemiadet(gender, hemoglobin)
    # Rest of the code for prediction
    input_array = np.array([[gender, hemoglobin]])
    return result

def send_anemia_json(result, data):
    report = Messages.anemia_message(result, data["hemoglobin"])
    return jsonify({
        "status": "success",
        "prediction": result,
        "report": report  
    })

def render_anemia_result(result, report):
    return render_template("result_anemia.html", prediction=result, report=report)


