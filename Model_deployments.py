#Library Importation
import pandas as pd
import joblib
import streamlit as st

# Load the model
model1 = joblib.load("car_loan_model.pkl")

# Streamlit UI
st.title("Car Loan Amount Prediction App")
st.write("Enter the required details to predict the car loan amount.")

st.sidebar.header("Customer Information")

# Collect user inputs
ASSET_COST = st.sidebar.number_input("Asset Cost (₦)", min_value=10000, max_value=10000000, step=1000)
PRIMARY_INSTAL_AMT = st.sidebar.number_input("Primary Installment Amount (₦)", min_value=1000, max_value=100000, step=500)
EMPLOYMENT_TYPE = st.sidebar.selectbox("Employment Type", ["Salaried", "Self Employed"])
CREDIT_HISTORY_LENGTH = st.sidebar.number_input("Credit History Length (months)", min_value=6, max_value=600, step=1)
Age = st.sidebar.number_input("Age", min_value=18, max_value=75, step=1)

# Convert categorical inputs
EMPLOYMENT_TYPE_Self_employed = 1 if EMPLOYMENT_TYPE == "Self Employed" else 0

# Prepare input data as DataFrame
input_data = pd.DataFrame([[ASSET_COST, PRIMARY_INSTAL_AMT, EMPLOYMENT_TYPE_Self_employed, CREDIT_HISTORY_LENGTH, Age]],
                          columns=['ASSET_COST', 'PRIMARY_INSTAL_AMT', 'EMPLOYMENT_TYPE_Self employed', 'CREDIT_HISTORY_LENGTH', 'Age'])

# Predict the loan amount
if st.sidebar.button("Predict Loan Amount"):
    prediction = model1.predict(input_data)[0]  # Using your best model directly
    st.success(f"Predicted Loan Amount: ₦{prediction:,.3f}")
