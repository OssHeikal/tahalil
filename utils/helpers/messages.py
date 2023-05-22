#masseges
class Messages:
    @staticmethod
    def anemia_message(result, hgl):
        if result == 'Negative':
            return f'''
            Your test results show a hemoglobin level of {hgl} g/dL, within the normal range, indicating adequate red blood cell count and oxygen-carrying capacity.\n\nHowever, note that anemia cannot be solely determined by hemoglobin levels, and further tests may be necessary for a comprehensive evaluation.\n\nThis automated analysis is not a substitute for professional medical advice. Consult a healthcare professional for accurate diagnosis and personalized guidance. Reach out to your healthcare provider with any questions or concerns.\n\nStay proactive in maintaining your health and continue practicing healthy lifestyle habits.
            '''
        elif result == 'Positive':
            return f'''
            With a hemoglobin level of {hgl} g/dL, your test indicates a low concentration of red blood cells, leading to anemia. Symptoms such as fatigue, weakness, shortness of breath, and pale skin may occur.\n\nIt is crucial to consult a healthcare professional for a detailed evaluation, further tests, and to identify the underlying cause. Treatment options, including dietary changes, iron supplementation, or addressing related health conditions, will be recommended.\n\nRemember, this automated analysis is not a substitute for professional medical advice. Reach out to your healthcare provider for personalized guidance and support in managing your condition.\n\nStay proactive and follow their recommendations for the best course of action.
            '''
        else:
            return "Invalid result value. Please provide valid data."

    @staticmethod
    def hepatitis_c_message(Age, ALB, ALP, ALT, AST, BIL, CHE, CHOL, CREA, GGT, PROT, sex,result):
        sex = 'Male' if sex == 1 else 'Female'
        if result == 'Negative':
            return f'''Based on your test results for Hepatitis C, it appears that you have tested negative. However, please note that Hepatitis C infection can have various stages and presentations, and further evaluation may be necessary.\n\nIt is recommended to consult a healthcare professional for a detailed assessment and to discuss any concerns you may have. They will provide accurate diagnosis, personalized guidance, and support.\n\nHere is the information about the input parameters:\n\u2022  Age: {Age}\n\u2022  Albumin (ALB) level: {ALB}\n\u2022  Alkaline Phosphatase (ALP) level: {ALP}\n\u2022  Alanine Aminotransferase (ALT) level: {ALT}\n\u2022  Aspartate Aminotransferase (AST) level: {AST}\n\u2022  Bilirubin (BIL) level: {BIL}\n\u2022  Cholinesterase (CHE) level: {CHE}\n\u2022  Cholesterol (CHOL) level: {CHOL}\n\u2022  Creatinine (CREA) level: {CREA}\n\u2022  Gamma-Glutamyl Transferase (GGT) level: {GGT}\n\u2022  Total Protein (PROT) level: {PROT}\n\u2022  Sex: {sex}\n\nRemember, this automated analysis is not a substitute for professional medical advice. Reach out to your healthcare provider for the best course of action tailored to your specific situation. Stay proactive in maintaining your health and follow their recommendations.
            '''
        elif result == 'Positive':
            return f'''
            Based on your test results for Hepatitis C, it appears that you have tested positive. Hepatitis C is a viral infection that affects the liver and can lead to liver damage if left untreated.\n\nIt is crucial to consult a healthcare professional experienced in managing Hepatitis C for further evaluation, including additional tests to assess the extent of the infection and the best treatment approach. They will provide personalized guidance, treatment options, and support.\n\nHere is the information about the input parameters:\n\u2022  Age: {Age}\n\u2022  Albumin (ALB) level: {ALB}\n\u2022  Alkaline Phosphatase (ALP) level: {ALP}\n\u2022  Alanine Aminotransferase (ALT) level: {ALT}\n\u2022  Aspartate Aminotransferase (AST) level: {AST}\n\u2022  Bilirubin (BIL) level: {BIL}\n\u2022  Cholinesterase (CHE) level: {CHE}\n\u2022  Cholesterol (CHOL) level: {CHOL}\n\u2022  Creatinine (CREA) level: {CREA}\n\u2022  Gamma-Glutamyl Transferase (GGT) level: {GGT}\n\u2022  Total Protein (PROT) level: {PROT}\n\u2022  Sex: {sex}\n\nRemember, this automated analysis is not a substitute for professional medical advice. Reach out to your healthcare provider to discuss your results and develop a comprehensive plan to manage your condition. Stay proactive and follow their recommendations for the best outcome.
            '''
        else:
            return "Invalid result value. Please provide valid data."
        
    @staticmethod
    def diabetes_message(age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level, smoking_history_current, smoking_history_former, gender,result):
        gender = 'Male' if gender == 1 else 'Female'
        hypertension = 'Yes' if hypertension == 1 else 'No'
        heart_disease = 'Yes' if heart_disease == 1 else 'No'
        smoking_history_current = 'Yes' if smoking_history_current == 1 else 'No'
        smoking_history_former = 'Yes' if smoking_history_former == 1 else 'No'
        if result == 'Negative':
            return f'''
            Based on your test results, it appears that you have tested negative for diabetes. However, it is important to note that diabetes can have different stages and presentations, and further evaluation may be necessary.\n\nIt is recommended to consult a healthcare professional for a detailed assessment and to discuss any concerns you may have. They will provide accurate diagnosis, personalized guidance, and support.\n\nHere is the information about the input parameters:\n\u2022  Age: {age}\nHypertension: {hypertension}\n\u2022  Heart Disease: {heart_disease}\n\u2022  BMI: {bmi}\n\u2022  HbA1c Level: {HbA1c_level} %\n\u2022  Blood Glucose Level: {blood_glucose_level} mg/dL\n\u2022  Smoking History (Current): {smoking_history_current}\n\u2022  Smoking History (Former): {smoking_history_former}\n\u2022  Gender: {gender}\n\nRemember, this automated analysis is not a substitute for professional medical advice. Reach out to your healthcare provider for the best course of action tailored to your specific situation. Stay proactive in maintaining your health and follow their recommendations.
            '''
        elif result == 'Positive':
            return f'''
            Based on your test results, it appears that you have tested positive for diabetes. Diabetes is a metabolic disorder characterized by high blood sugar levels.\n\nIt is crucial to consult a healthcare professional experienced in managing diabetes for further evaluation, including additional tests to determine the severity of the condition and develop an appropriate treatment plan. They will provide personalized guidance, lifestyle recommendations, and support.\n\nHere is the information about the input parameters:\n\u2022  Age: {age}\n\u2022  Hypertension: {hypertension}\n\u2022  Heart Disease: {heart_disease}\n\u2022  BMI: {bmi}\n\u2022  HbA1c Level: {HbA1c_level} %\n\u2022  Blood Glucose Level: {blood_glucose_level} mg/dL\n\u2022  Smoking History (Current): {smoking_history_current}\n\u2022  Smoking History (Former): {smoking_history_former}\n\u2022  Gender: {gender}\n\nRemember, this automated analysis is not a substitute for professional medical advice. Reach out to your healthcare provider to discuss your results and develop a comprehensive plan to manage your condition. Stay proactive and follow their recommendations for the best outcome.
            '''
        #else:
         #   return "Invalid result value. Please provide valid data."
    
    
    @staticmethod
    def heart_disease_message(result,ST_Slope_Up, Oldpeak, Cholesterol, ExerciseAngina_Y, MaxHR, Sex_M, Age, RestingBP):
        Sex_M = 'Male' if Sex_M == 1 else 'Female'
        ExerciseAngina_Y = 'Yes' if ExerciseAngina_Y == 1 else 'No'
        ST_Slope_Up = 'Up' if ST_Slope_Up == 1 else 'Flate'
        if result == 'Negative':
            return f'''
            Based on your test results, it appears that you have tested negative for heart disease. However, please note that the absence of heart disease cannot be definitively determined by a single test.\n\nIt is recommended to consult a healthcare professional for a comprehensive evaluation, considering additional factors and tests specific to your situation. They will provide accurate diagnosis, personalized guidance, and support.\n\nHere is the information about the input parameters:\n\u2022  ST Slope : {ST_Slope_Up}\n\u2022  Oldpeak: {Oldpeak}\n\u2022  Cholesterol: {Cholesterol}\n\u2022  Exercise-Induced Angina: {ExerciseAngina_Y}\n\u2022  Max Heart Rate: {MaxHR}\n\u2022  Sex: {Sex_M}\n\u2022  Age: {Age}\n\u2022  Resting Blood Pressure: {RestingBP}\n\nRemember, this automated analysis is not a substitute for professional medical advice. Reach out to your healthcare provider for the best course of action tailored to your specific situation. Stay proactive in maintaining your health and follow their recommendations.
            '''
        elif result == 'Positive':
            return f'''
            Based on your test results, it appears that you have tested positive for heart disease. Heart disease refers to various conditions that affect the heart and its blood vessels.\n\nIt is crucial to consult a healthcare professional experienced in managing heart disease for further evaluation, including additional tests to assess the severity of the condition and develop an appropriate treatment plan. They will provide personalized guidance, lifestyle recommendations, and support.\n\nHere is the information about the input parameters:\n\u2022  ST Slope: {ST_Slope_Up}\n\u2022  Oldpeak: {Oldpeak}\n\u2022  Cholesterol: {Cholesterol}\n\u2022  Exercise-Induced Angina: {ExerciseAngina_Y}\n\u2022  Max Heart Rate: {MaxHR}\n\u2022  Sex: {Sex_M}\n\u2022  Age: {Age}\n\u2022  Resting Blood Pressure: {RestingBP}\n\nRemember, this automated analysis is not a substitute for professional medical advice. Reach out to your healthcare provider to discuss your results and develop a comprehensive plan to manage your condition. Stay proactive and follow their recommendations for the best outcome.
            '''
        else:
            return "Invalid result value. Please provide valid data."
        
    @staticmethod    
    def hepatitis_b_message(surface_antigen, surface_antibody, core_antibody, result):
        surface_antigen = 'Positive' if surface_antigen == 1 else 'Negative'
        surface_antibody = 'Positive' if surface_antibody == 1 else 'Negative'
        core_antibody = 'Positive' if core_antibody == 1 else 'Negative'
        if result == 0:
            return f'''
            Based on your test results, it appears that you are not immune to hepatitis B.\n\nHere is the information about the input parameters:\n\u2022  Surface Antigen: {surface_antigen}\n\u2022  Surface Antibody: {surface_antibody}\n\u2022  Core Antibody: {core_antibody}\n\nInterpretation:\nThis result indicates that you have not been infected with the hepatitis B virus and are at risk of possible infection.\n\nAction Needed:\nIt is recommended to get vaccinated against hepatitis B to protect against future infection. Consult a healthcare professional for further guidance.
            '''
        elif result == 1:
            return f'''
            Based on your test results, it appears that you are immune and protected against hepatitis B.\n\nHere is the information about the input parameters:\n\u2022  Surface Antigen: {surface_antigen}\n\u2022  Surface Antibody: {surface_antibody}\n\u2022  Core Antibody: {core_antibody}\n\nInterpretation:\nThis result indicates that you have been vaccinated against hepatitis B, have no current infection, and have never been infected in the past.\n\nAction Needed:\nNo vaccine is needed as you are already protected. However, it is still advisable to maintain regular healthcare check-ups and follow any specific recommendations from a healthcare professional.
            '''
        elif result == 2:
            return f'''
            Based on your test results, it appears that you are immune and protected against hepatitis B.\n\nHere is the information about the input parameters:\n\u2022  Surface Antigen: {surface_antigen}\n\u2022  Surface Antibody: {surface_antibody}\n\u2022  Core Antibody: {core_antibody}\n\nInterpretation:\nThe presence of hepatitis B surface antibodies (HBsAb) suggests that you have recovered from a past hepatitis B infection and are now immune to the virus. You cannot infect others.\nAction Needed:\nNo vaccine is needed since you are already protected. Regular monitoring and follow-up with a healthcare professional may be advisable.
            '''
        elif result == 3:
            return f'''
            Based on your test results, it appears that you could be infected with hepatitis B.\n\nHere is the information about the input parameters:\n\u2022  Surface Antigen: {surface_antigen}\n\u2022  Surface Antibody: {surface_antibody}\n\u2022  Core Antibody: {core_antibody}\n\nInterpretation:\nThe result is inconclusive, indicating the possibility of a past or current hepatitis B infection.\n\nAction Needed:\nIt is recommended to consult a healthcare professional who specializes in hepatitis B for further evaluation. Additional testing is necessary to determine the presence or absence of the virus and to guide appropriate actions and follow-up care.
            '''
        elif result == 4:
            return f'''
            Based on your test results, it appears that you are currently infected with hepatitis B.\n\nHere is the information about the input parameters:\n\u2022  Surface Antigen: {surface_antigen}\n\u2022  Surface Antibody: {surface_antibody}\n\u2022  Core Antibody: {core_antibody}\n\nInterpretation:\nA positive result for HBsAg suggests that you are currently infected with the hepatitis B virus. The virus can be contagious and spread to others.\n\nAction Needed:\nIt is crucial to seek immediate medical attention and find a doctor who is knowledgeable about hepatitis B for further evaluation, treatment, and management. More testing may be necessary to assess the extent of the infection and determine the appropriate course of action.
            '''
        else:
            return "Invalid result value. Please provide valid data."