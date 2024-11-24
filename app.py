import streamlit as st
import numpy as np
import pickle

# Load the model
with open('model.pkl', 'rb') as file:
    classifier = pickle.load(file)

# Define reasons for health issues
reasons = {
    0: "Normal: No health issue detected.",
    1: "Mild: Possible dehydration or minor symptoms.",
    2: "Severe: Requires immediate attention due to significant health concerns.",
    3: "Chronic: Persistent condition that requires long-term management."
}

# Streamlit app title and description
st.title("Health Monitoring Application")
st.markdown("""
This application predicts the severity of a health condition based on your inputs and provides possible reasons for the result.
""")

# Collect user input
st.subheader("Enter Health Parameters")
dehydration = st.number_input("Dehydration (0: No, 1: Yes)", min_value=0, max_value=1, value=0)
medicine_overdose = st.number_input("Medicine Overdose (0: No, 1: Yes)", min_value=0, max_value=1, value=0)
acidious = st.number_input("Acidious (0: No, 1: Yes)", min_value=0, max_value=1, value=0)
cold = st.number_input("Cold (0: No, 1: Yes)", min_value=0, max_value=1, value=0)
cough = st.number_input("Cough (0: No, 1: Yes)", min_value=0, max_value=1, value=0)
temperature = st.number_input("Temperature (°F)", min_value=90, max_value=120, value=98)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=80)
pulse = st.number_input("Pulse", min_value=40, max_value=120, value=70)
bpsys = st.number_input("BPSYS (Systolic Blood Pressure)", min_value=80, max_value=200, value=120)
bpdia = st.number_input("BPDIA (Diastolic Blood Pressure)", min_value=50, max_value=120, value=80)
respiratory_rate = st.number_input("Respiratory Rate (breaths per minute)", min_value=10, max_value=40, value=20)
oxygen_saturation = st.number_input("Oxygen Saturation (decimal)", min_value=0.0, max_value=1.0, value=0.95)
ph = st.number_input("PH Level (decimal)", min_value=6.0, max_value=8.0, value=7.4)

# Prepare data for prediction
input_data = np.array([dehydration, medicine_overdose, acidious, cold, cough, temperature, heart_rate, pulse, bpsys, bpdia, respiratory_rate, oxygen_saturation, ph])
print(f"length: {len(input_data)}")
input_data_reshaped = input_data.reshape(1, -1)

# Predict and display results
if st.button("Predict"):
    prediction = classifier.predict(input_data_reshaped)

    if prediction[0] == 0:
        severity = "Normal"
    elif prediction[0] == 1:
        severity = "Mild"
    elif prediction[0] == 2:
        severity = "Severe"
    elif prediction[0] == 3:
        severity = "Chronic"
    
    st.subheader(f"Prediction: {severity}")
    st.write(reasons[prediction[0]])