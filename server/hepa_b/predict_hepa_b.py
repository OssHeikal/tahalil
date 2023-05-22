import numpy as np
import pickle

import pandas as pd
from flask import jsonify, render_template
from utils.helpers.messages import Messages


def Hb_prediction(surface_antigen, surface_antibody, core_antibody):
    features = [[surface_antigen, surface_antibody, core_antibody]]
    features = np.array(features, dtype=bool)
    model3 = pickle.load(open("server/hepa_b/HB.pkl", "rb"))
    pred = model3.predict(features)
    class_pred = pred[0]
    return class_pred

def predict_hepatitis_b(data):
    surface_antigen = int(data["surface_antigen"])
    surface_antibody = int(data["surface_antibody"])
    core_antibody = int(data["core_antibody"])
    result = Hb_prediction(surface_antigen, surface_antibody, core_antibody)
    # Rest of the code for prediction
    input_array = np.array([[surface_antigen, surface_antibody, core_antibody]])
    result = 5 if surface_antigen == 1 and surface_antibody == 1 and core_antibody == 1 else result
    return result

def send_hepatitis_b_json(result, data):
    report = Messages.hepatitis_b_message(data["surface_antigen"], data["surface_antibody"], data["core_antibody"], result)
    return jsonify({
        "status": "success",
        "prediction": 'Not Protected' if result == 0 else 'protected' if result == 1 else 'protected' if result == 2 else 'May be Infected' if result == 3 else 'Infected' if result == 4 else 'Invalid',
        "report": Messages.hepatitis_b_message(data["surface_antigen"], data["surface_antibody"], data["core_antibody"], result)
    })

def render_hepatitis_b_result(result, report):
    result = 'Not Protected' if result == 0 else 'protected' if result == 1 else 'protected' if result == 2 else 'May be Infected' if result == 3 else 'Infected' if result == 4 else 'Invalid'
    return render_template("result_Hb.html", prediction=result, report=report)