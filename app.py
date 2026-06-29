import streamlit as st
import joblib
import pandas as pd

st.title("Heart Disease Risk Predictor")

model = joblib.load("heart_disease_model.pkl")
scaler = joblib.load("heart_disease_scaler.pkl")

st.header("Enter Patient Information")

age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", [1, 2, 3, 4])
trestbps = st.number_input("Resting Blood Pressure", min_value=80, max_value=220, value=120)
chol = st.number_input("Cholesterol", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
restecg = st.selectbox("Resting ECG Result", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", min_value=60, max_value=220, value=150)
exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
slope = st.selectbox("Slope of Peak Exercise ST Segment", [1, 2, 3])
ca = st.selectbox("Number of Major Vessels Colored", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia", [3, 6, 7])

if st.button("Predict"):
    # Convert dropdown text answers into the numbers the model expects
    sex_num = 1 if sex == "Male" else 0
    fbs_num = 1 if fbs == "Yes" else 0
    exang_num = 1 if exang == "Yes" else 0

    # Build one row matching the exact column order the model was trained on
    patient = pd.DataFrame([[age, sex_num, cp, trestbps, chol, fbs_num,
                              restecg, thalach, exang_num, oldpeak,
                              slope, ca, thal]],
                            columns=['age','sex','cp','trestbps','chol','fbs',
                                     'restecg','thalach','exang','oldpeak',
                                     'slope','ca','thal'])

    patient_scaled = scaler.transform(patient)
    prediction = model.predict(patient_scaled)[0]
    probability = model.predict_proba(patient_scaled)[0][1]

    if prediction == 1:
        st.error(f"High risk of heart disease — {probability*100:.1f}% probability")
    else:
        st.success(f"Low risk of heart disease — {probability*100:.1f}% probability")