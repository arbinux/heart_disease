import streamlit as st
import requests

st.title("Heart Disease Prediction")

st.write("Enter details below")


age = st.slider("Age", 18, 100, 40)

sex = st.selectbox("Sex", ["M","F"])

chest_pain = st.selectbox(
    "Chest Pain Type",
    ["ATA","NAP","TA","ASY"]
)

resting_bp = st.number_input(
    "Resting Blood Pressure",
    80,200,120
)

cholesterol = st.number_input(
    "Cholesterol",
    100,600,200
)

fasting_bs = st.selectbox(
    "Fasting Blood Sugar > 120",
    [0,1]
)

resting_ecg = st.selectbox(
    "Resting ECG",
    ["Normal","ST","LVH"]
)

max_hr = st.slider(
    "Max Heart Rate",
    60,220,150
)

exercise_angina = st.selectbox(
    "Exercise Angina",
    ["Y","N"]
)

oldpeak = st.slider(
    "Oldpeak",
    0.0,6.0,1.0
)

st_slope = st.selectbox(
    "ST Slope",
    ["Up","Flat","Down"]
)


if st.button("Predict"):


    data = {

        "Age": age,
        "Sex": sex,
        "ChestPainType": chest_pain,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "RestingECG": resting_ecg,
        "MaxHR": max_hr,
        "ExerciseAngina": exercise_angina,
        "Oldpeak": oldpeak,
        "ST_Slope": st_slope

    }


    response = requests.post(

        "https://heart-diease.onrender.com/predict",

        json=data

    )


    result = response.json()


    if result["prediction"] == "High Risk of Heart Disease":

        st.error(result["prediction"])

    else:

        st.success(result["prediction"])
