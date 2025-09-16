import streamlit as st
import numpy as np
import joblib

# Load saved model
model = joblib.load("temperature_model.pkl")

st.title("🌞 IoT Sensor Data Prediction App")

# User Inputs
solar = st.number_input("Enter Solar Irradiance", min_value=0.0)
wind = st.number_input("Enter Wind Speed (m/s)", min_value=0.0)

if st.button("Predict Temperature"):
    input_data = np.array([[solar, wind]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Outdoor Temperature: {prediction[0]:.2f} °C")
