import numpy as np
import pickle
from flask import jsonify, render_template
from utils.helpers.messages import Messages



def Hepatitis_cpredict(Age, ALB, ALP, ALT, AST, BIL, CHE, CHOL, CREA, GGT, PROT, sex):
    classes = ["Negative", "Positive"]
    model4 = pickle.load(open("server/hepa_c/HC.pkl", "rb"))
    pred = model4.predict([[Age, ALB, ALP, ALT, AST, BIL, CHE, CHOL, CREA, GGT, PROT, sex]])
    class_pred = classes[pred[0]]
    return class_pred


def predict_hepatitis_c(data):
    Age = int(data["age"])
    ALB = float(data["alb"])
    ALP = float(data["alp"])
    ALT = float(data["alt"])
    AST = float(data["ast"])
    BIL = float(data["bil"])
    CHE = float(data["che"])
    CHOL = float(data["chol"])
    CREA = float(data["crea"])
    GGT = float(data["ggt"])
    PROT = float(data["prot"])
    sex = float(data["sex"])  # Ensure consistent data type
    result = Hepatitis_cpredict(Age, ALB, ALP, ALT, AST, BIL, CHE, CHOL, CREA, GGT, PROT, sex)
    return result


def send_hepatitis_c_json(result, data):
    report = Messages.hepatitis_c_message(data['age'], data['alb'], data['alp'], data['alt'], data['ast'], data['bil'], data['che'], data['chol'], data['crea'], data['ggt'], data['prot'], data['sex'], result)
    return jsonify({
        "status": "success",
        "prediction": result,
        "report": report
    })


def render_hepatitis_c_result(result, report):
    return render_template("result_HC.html", prediction=result, report=report)
