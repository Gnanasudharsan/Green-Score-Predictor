import streamlit as st
import pandas as pd
from codecarbon import EmissionsTracker

st.set_page_config(page_title="Green Score Predictor", layout="centered")
st.title("🌱 Green Score Predictor for AI Models")

st.markdown("""
This tool estimates the energy usage and carbon footprint of training a machine learning model.
Just enter your training setup below:
""")

# --- User Inputs ---
model_name = st.selectbox("Select Model Architecture", ["BERT", "DistilBERT", "ResNet", "Custom"])
dataset_size = st.number_input("Dataset Size (in GB)", min_value=0.1, step=0.1)
training_time = st.number_input("Training Duration (in hours)", min_value=0.1, step=0.1)
hardware_type = st.selectbox("Hardware Used", ["CPU", "GPU: NVIDIA A100", "GPU: NVIDIA V100", "TPU"])
num_devices = st.slider("Number of Devices Used", 1, 8, 1)

if st.button("Estimate Green Score"):
    # --- Simulate emissions calculation ---
    energy_kwh = training_time * num_devices * (0.4 if "GPU" in hardware_type else 0.2)  # Simplified estimate
    co2_emissions = energy_kwh * 0.5  # kg CO2 per kWh

    # --- Assign a Green Score ---
    if co2_emissions < 5:
        score = "A"
    elif co2_emissions < 10:
        score = "B"
    elif co2_emissions < 20:
        score = "C"
    elif co2_emissions < 30:
        score = "D"
    else:
        score = "E"

    st.subheader("Results")
    st.write(f"**Estimated Energy Usage:** {energy_kwh:.2f} kWh")
    st.write(f"**Estimated CO₂ Emissions:** {co2_emissions:.2f} kg CO₂e")
    st.write(f"**Green Score:** {score}")

    if model_name == "BERT":
        st.info("✅ Tip: Consider using DistilBERT for a smaller footprint (~40% less compute).")
    elif model_name == "ResNet":
        st.info("✅ Tip: Try EfficientNet for better energy-performance tradeoff.")
