import streamlit as st
import pandas as pd
import joblib

# Load trained model
pipe = joblib.load("models/laptop_price_pipe.pkl")

st.title("💻 Laptop Price Predictor")

# Input form
company = st.selectbox("Company", ['Dell', 'HP', 'Lenovo', 'Apple', 'Asus', 'Acer', 'MSI', 'Other'])
typename = st.selectbox("Type", ['Ultrabook', 'Gaming', 'Notebook', '2 in 1 Convertible', 'Workstation', 'Other'])
cpu = st.selectbox("CPU Brand", ['Intel', 'AMD', 'Other'])
gpu = st.selectbox("GPU Brand", ['Nvidia', 'AMD', 'Intel', 'Other'])
ram = st.slider("RAM (GB)", 2, 64, 8)
inches = st.slider("Screen Size (inches)", 10.0, 18.0, 15.6)
ppi = st.number_input("PPI (Pixels Per Inch)", min_value=50, max_value=400, value=141)
is_touch = st.selectbox("Touchscreen?", [0, 1])
is_ips = st.selectbox("IPS Panel?", [0, 1])
storage = st.slider("Total Storage (GB)", 128, 4000, 512)

if st.button("Predict Price"):
    # Create DataFrame
    input_df = pd.DataFrame([{
        "Company": company,
        "TypeName": typename,
        "cpu_brand": cpu,
        "gpu_brand": gpu,
        "Ram": ram,
        "Inches": inches,
        "ppi": ppi,
        "is_touch": is_touch,
        "is_ips": is_ips,
        "total_storage_gb": storage
    }])

    # Predict
    prediction = pipe.predict(input_df)[0]
    st.success(f"💰 Estimated Laptop Price: ₹ {int(prediction):,}")
