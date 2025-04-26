import streamlit as st
import pandas as pd

# Hardware options with average power consumption in Watts
hardware_options = {
    "NVIDIA RTX 4090": 450,
    "NVIDIA RTX 4080": 320,
    "NVIDIA RTX 4070": 200,
    "NVIDIA A100": 400,
    "NVIDIA V100": 300,
    "NVIDIA T4 Tensor Core": 70,
    "NVIDIA H100": 700,
    "NVIDIA P100": 250,
    "Google TPU v2": 280,
    "Google TPU v3": 300,
    "Google TPU v4": 350,
    "Google TPU v5": 400,
    "Apple M1 Chip": 30,
    "Apple M2 Chip": 35,
    "Intel Xeon CPU": 85,
    "Intel Xeon Platinum": 105,
    "AMD EPYC CPU": 120,
    "AMD Ryzen 9": 105,
    "Intel Core i9": 125,
    "Intel Core i7": 95,
    "Intel Core i5": 65,
    "AMD Ryzen 7": 95,
    "AMD Ryzen 5": 65,
    "AWS Inferentia": 75,
    "AWS Trainium": 150,
    "Google TPU Edge": 15,
    "Qualcomm Cloud AI 100": 70,
    "IBM Power9": 190,
    "ARM Neoverse": 60,
    "Other (Custom)": None
}

# Model options and greener alternatives
green_alternatives = {
    "BERT": "DistilBERT",
    "GPT-2": "GPT-2 Small",
    "GPT-3": "GPT-2 Large",
    "RoBERTa": "TinyBERT",
    "T5-Base": "T5-Small",
    "T5-Large": "T5-Base",
    "XLNet": "ALBERT",
    "Albert": "TinyAlbert",
    "DistilBERT": "MobileBERT",
    "MobileNetV2": "EfficientNet-Lite",
    "ResNet-50": "MobileNetV2",
    "ResNet-101": "EfficientNet",
    "InceptionV3": "EfficientNet",
    "DenseNet-121": "EfficientNet",
    "VGG16": "MobileNet",
    "EfficientNet-B0": "EfficientNet-Lite0",
    "ViT-Base": "DeiT",
    "DeiT": "DeiT-Tiny",
    "Swin Transformer": "MobileViT",
    "YOLOv5": "YOLOv5n",
    "YOLOv7": "YOLOv5s",
    "Faster R-CNN": "EfficientDet",
    "Transformer-XL": "Lite Transformer",
    "Pegasus": "T5-Base",
    "MarianMT": "TinyMT",
    "BLOOM": "OPT",
    "OPT": "OPT-Small",
    "LLaMA": "LLaMA-2 7B",
    "Whisper": "Tiny Whisper",
    "Other (Custom)": None
}

st.title("🌱 Green Score Predictor for AI Models")

# Inputs
model_name = st.selectbox("Select your Model", list(green_alternatives.keys()))
dataset_size_gb = st.number_input("Enter Dataset Size (in GB)", min_value=0.0)
hardware_selected = st.selectbox("Select your Hardware", list(hardware_options.keys()))
number_of_devices = st.number_input("Enter Number of Devices (GPUs/CPUs/TPUs used)", min_value=1, value=1)
training_hours = st.number_input("Enter Training Duration (hours)", min_value=0.0)

# If custom hardware is selected
if hardware_selected == "Other (Custom)":
    power_consumption = st.number_input("Enter your Device's Power Consumption (Watts)", min_value=1)
else:
    power_consumption = hardware_options[hardware_selected]

# If custom model is selected
if model_name == "Other (Custom)":
    model_name = st.text_input("Enter your Model Name")

# Button to calculate
if st.button("Calculate Green Score"):
    if power_consumption is None or training_hours == 0:
        st.error("Please provide valid inputs!")
    else:
        total_energy_kwh = (power_consumption * training_hours * number_of_devices) / 1000  # Watts to kWh
        co2_emission_kg = total_energy_kwh * 0.475  # Global average kg CO2 per kWh

        # Assign Green Score
        if co2_emission_kg < 50:
            green_score = "A"
        elif co2_emission_kg < 150:
            green_score = "B"
        elif co2_emission_kg < 300:
            green_score = "C"
        elif co2_emission_kg < 500:
            green_score = "D"
        else:
            green_score = "E"

        # Display results
        st.success(f"🌿 Estimated Energy Consumption: {total_energy_kwh:.2f} kWh")
        st.success(f"🌍 Estimated CO₂ Emissions: {co2_emission_kg:.2f} kg")
        st.success(f"🏆 Green Score: {green_score}")

        # Suggest greener alternative
        suggestion = green_alternatives.get(model_name.strip(), None)
        if suggestion:
            st.info(f"💡 Consider switching from **{model_name}** to **{suggestion}** for better efficiency!")
        else:
            st.info("ℹ️ No alternative suggestion found for this model.")

# Optionally, allow downloading the result
if st.button("Download Results"):
    results = pd.DataFrame({
        "Model": [model_name],
        "Dataset Size (GB)": [dataset_size_gb],
        "Hardware": [hardware_selected],
        "Number of Devices": [number_of_devices],
        "Training Hours": [training_hours],
        "Energy Consumption (kWh)": [total_energy_kwh],
        "CO2 Emissions (kg)": [co2_emission_kg],
        "Green Score": [green_score]
    })
    csv = results.to_csv(index=False)
    st.download_button(
        label="📥 Download results as CSV",
        data=csv,
        file_name="green_score_results.csv",
        mime="text/csv"
    )
