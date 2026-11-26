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


@st.cache_data(show_spinner=False)
def run_optimization(h2):
    """Cache results for H₂ values that have already been optimised."""
    return optimize(h2)


h2 = st.number_input(
    "Enter Available H₂ Feed Flow",
    min_value=0.92,
    max_value=5.39,
    value=3.00,
    step=0.01,
    format="%.2f",
    help="The allowed range matches the H₂ values seen during training.",
)

if st.button("Optimize"):

    try:
        with st.spinner("Searching for the best operating conditions..."):
            result = run_optimization(h2)
    except ValueError as exc:
        st.error(f"Optimization could not be completed: {exc}")
    else:
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
