import numpy as np
from flask import Flask, render_template, request

from server.anemia.predict_anemia import predict_anemia, render_anemia_result, send_anemia_json
from server.hepa_b.predict_hepa_b import predict_hepatitis_b, render_hepatitis_b_result, send_hepatitis_b_json
from server.hepa_c.predict_hepa_c import predict_hepatitis_c, render_hepatitis_c_result, send_hepatitis_c_json
from server.diabetes.predict_diabetes import predict_diabetes, render_diabetes_result, send_diabetes_json
from server.heart_disease.predict_heart_disease import predict_heart_disease, render_heart_result, send_herat_json
from utils.helpers.messages import Messages


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('welcome_screen.html')

@app.route('/heart_disease')
def heart_disease():
    return render_template('heart_disease.html')


@app.route('/hepatitis_b')
def hepatitis_b():
    return render_template('hepatitis_b.html')


@app.route('/hepatitis_c')
def hepatitis_c():
    return render_template('hepatitis_c.html')


@app.route('/anemia', methods=['GET'])
def anemia():
    return render_template('anemia.html')


@app.route('/diabetes')
def diabetes():
    return render_template('diabetes.html')


@app.route('/predict/anemia', methods=['POST'])
def predict_anemia_endpoint():
    content_type = request.headers.get('Content-Type')
    if content_type.startswith('application/json'):
        data = request.get_json()
        result = predict_anemia(data)
        return send_anemia_json(result, data)
    else:
        data = request.form
        result = predict_anemia(data)
        report = Messages.anemia_message(result, data["hemoglobin"])
        return render_anemia_result(result=result, report=report)


@app.route('/predict_diabetes', methods=['POST'])
def predict_diabetes_endpoint():
    content_type = request.headers.get('Content-Type')
    if content_type.startswith('application/json'):
        data = request.get_json()
        result=predict_diabetes(data)
        return send_diabetes_json(result, data)
    else:
        data = request.form
        result = predict_diabetes(data)
        report = Messages.diabetes_message(data['age'], data['hypertension'], data['heart_disease'], data['bmi'], data['HbA1c_level'], data['blood_glucose_level'], data['smoking_history_current'], data['smoking_history_former'], data['gender'], result)
        return render_diabetes_result(result=result, report=report)

@app.route('/predict/hepatitis_b', methods=['POST'])
def predict_hepatitis_b_endpoint():
    content_type = request.headers.get('Content-Type')
    if content_type.startswith('application/json'):
        data = request.get_json()
        result = predict_hepatitis_b(data)
        return send_hepatitis_b_json(result, data)
    else:
        data = request.form
        result = predict_hepatitis_b(data)
        report = Messages.hepatitis_b_message(data["surface_antigen"], data["surface_antibody"], data["core_antibody"], result)
        return render_hepatitis_b_result(result=result, report=report)

@app.route('/predict/hepatitis_c', methods=['POST'])
def predict_hepatitis_c_endpoint():
    content_type = request.headers.get('Content-Type')
    if content_type.startswith('application/json'):
        data = request.get_json()
        result = predict_hepatitis_c(data)
        return send_hepatitis_c_json(result, data)
    else:
        data = request.form
        result = predict_hepatitis_c(data)
        report = Messages.hepatitis_c_message(data['age'], data['alb'], data['alp'], data['alt'], data['ast'], data['bil'], data['che'], data['chol'], data['crea'], data['ggt'], data['prot'], data['sex'], result)
        return render_hepatitis_c_result(result=result, report=report)


@app.route('/predict/heart_disease', methods=['POST'])
def predict_heart_disease_endpoint():
    content_type = request.headers.get('Content-Type')
    if content_type.startswith('application/json'):
        data = request.get_json()
        result = predict_heart_disease(data)
        return send_herat_json(result, data)
    else:
        data = request.form
        result = predict_heart_disease(data)
        report = Messages.heart_disease_message(result,data['ST_Slope_Up'], data['Oldpeak'],data['Cholesterol'] ,data['ExerciseAngina_Y'], data['MaxHR'], data['Sex_M'], data['Age'], data['RestingBP'] )
        return render_heart_result(result=result, report=report)


if __name__ == '__main__':
    app.run()
