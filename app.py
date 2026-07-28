import streamlit as st
from optimizer import optimize

st.set_page_config(
    page_title="AI Methanol Optimizer",
    page_icon="⚗️",
    layout="centered"
)

st.title("AI-Based Methanol Production Optimizer")

st.write(
    "Enter the available H₂ feed flow. "
    "The AI model will recommend the best operating conditions "
    "to maximize methanol production."
)
h2 = st.number_input(
    "Enter Available H₂ Feed Flow",
    min_value=0.90,
    max_value=5.40,
    value=3.00,
    step=0.01,
    format="%.2f"
)
# add button for optimization
if st.button("Optimize"):

    result = optimize(h2)

    st.success("Optimal Operating Conditions Found!")

    st.write("### Recommended Operating Conditions")

    st.write(f"Available H₂ : {result['H2']:.2f}")
    st.write(f"Recommended CO₂ : {result['CO2']:.4f}")
    st.write(f"H₂/CO₂ Ratio : {result['Ratio']:.2f}")
    st.write(f"Temperature : {result['Temperature']:.2f} °C")
    st.write(f"Pressure : {result['Pressure']:.2f} bar")
    st.write(f"Time Cost : {result['TimeCost']:.2f} hr")

    st.write("### Predicted Methanol Production")

    st.metric(
        label="Maximum Predicted Methanol",
        value=f"{result['PredictedMethanol']:.6f}"
    )