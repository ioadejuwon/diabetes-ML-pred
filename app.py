import streamlit as st
import pickle
import numpy as np

# Load model
# with open("best_model.pkl", "rb") as f:
#     model = pickle.load(f)
try:
    with open("best_model.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.write("Error loading model:")
    st.write(e)
    

# Load scaler
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

st.title("Diabetes Prediction App")
st.write("Enter patient details below to predict diabetes status.")

# User-friendly labels mapped to model values
gender_options = {
    "Female": 0,
    "Male": 1
}

hypertension_options = {
    "No": 0,
    "Yes": 1
}

heart_disease_options = {
    "No": 0,
    "Yes": 1
}

smoking_history_options = {
    "Never": 0,
    "Currently Smoking": 1,
    "Ever": 1,
    "Not Currently Smoking": 1,
    "Former": 1,
    "No Info": -1
}

# Form inputs
gender_label = st.selectbox("Gender", list(gender_options.keys()))
age = st.number_input("Age", min_value=1, max_value=120, value=25)
hypertension_label = st.selectbox("History of Hypertension", list(hypertension_options.keys()))
# heart_disease_label = st.selectbox("History of Heart Disease", list(heart_disease_options.keys()))
smoking_history_label = st.selectbox("Smoking History", list(smoking_history_options.keys()))
bmi = st.number_input("Body Mass Index (BMI)", min_value=0.0, value=20.0, step=0.01)
HbA1c_level = st.number_input("Hemoglobin A1c Level", min_value=0.0, value=5.0, step=0.01)
blood_glucose_level = st.number_input("Blood Glucose Level", min_value=0.0, value=100.0, step=0.01)

if st.button("Predict"):
    gender = gender_options[gender_label]
    hypertension = hypertension_options[hypertension_label]
    # heart_disease = heart_disease_options[heart_disease_label]
    smoking_history = smoking_history_options[smoking_history_label]

    input_data = np.array([[
        gender,
        age,
        hypertension,
        # heart_disease,
        smoking_history,
        bmi,
        HbA1c_level,
        blood_glucose_level
    ]])

    input_data_scaled = scaler.transform(input_data)
    prediction = model.predict(input_data_scaled)[0]

    if prediction == 0:
        prediction_label = "No diabetes"
    else:
        prediction_label = "Diabetes"

    st.subheader("Result")
    st.success(prediction_label)