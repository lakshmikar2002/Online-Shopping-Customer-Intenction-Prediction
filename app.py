import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("model.pkl")

st.set_page_config(page_title="Purchase Prediction", layout="centered")

st.title("🛒 Online Shopper Purchase Prediction")

st.write("Enter user session details:")

# =========================
# INPUTS
# =========================

Administrative_Duration = st.number_input("Administrative Duration", 0.0)
Informational_Duration = st.number_input("Informational Duration", 0.0)
ProductRelated = st.number_input("Product Related Pages", 0)
ProductRelated_Duration = st.number_input("Product Related Duration", 0.0)
BounceRates = st.number_input("Bounce Rates", 0.0)
ExitRates = st.number_input("Exit Rates", 0.0)
PageValues = st.number_input("Page Values", 0.0)
SpecialDay = st.slider("Special Day", 0.0, 1.0)

Month = st.selectbox("Month", [
    "Feb","Mar","May","June","Jul","Aug","Sep","Oct","Nov","Dec"
])

OperatingSystems = st.number_input("Operating Systems", 1)
Browser = st.number_input("Browser", 1)
Region = st.number_input("Region", 1)
TrafficType = st.number_input("Traffic Type", 1)

VisitorType = st.selectbox(
    "Visitor Type",
    ["Returning_Visitor", "New_Visitor", "Other"]
)

Weekend = st.selectbox("Weekend", [True, False])

# =========================
# PREDICTION
# =========================
if st.button("Predict"):

    input_data = pd.DataFrame([{
        'Administrative_Duration': Administrative_Duration,
        'Informational_Duration': Informational_Duration,
        'ProductRelated': ProductRelated,
        'ProductRelated_Duration': ProductRelated_Duration,
        'BounceRates': BounceRates,
        'ExitRates': ExitRates,
        'PageValues': PageValues,
        'SpecialDay': SpecialDay,
        'Month': Month,
        'OperatingSystems': OperatingSystems,
        'Browser': Browser,
        'Region': Region,
        'TrafficType': TrafficType,
        'VisitorType': VisitorType,
        'Weekend': Weekend
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.success(f"✅ Customer WILL Purchase (Confidence: {probability:.2f})")
    else:
        st.error(f"❌ Customer will NOT Purchase (Confidence: {probability:.2f})")