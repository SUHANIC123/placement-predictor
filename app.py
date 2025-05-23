import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Placement Predictor")

GPA = st.number_input("Enter GPA")
backlogs = st.number_input("Enter number of backlogs", step=1)

if st.button("Check Eligibility"):
    if GPA > 8.5 and backlogs == 0:
        result = "Eligible"
    else:
        prediction = model.predict([[GPA, backlogs]])
        result = "Eligible" if prediction[0] == 1 else "Not Eligible"
    st.success(f"Prediction: {result}")

