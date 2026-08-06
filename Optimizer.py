import joblib
import numpy as np

# Load trained model
from pathlib import Path
import joblib

MODEL_PATH = Path(__file__).parent / "methanol_gbr_model.pkl"
model = joblib.load(MODEL_PATH)


def optimize(h2):

    # Store best result
    best_methanol = -float("inf")
    best_conditions = None

    # Search ranges
    ratio_values = np.linspace(2.0, 4.5, 20)

    temp_values = np.linspace(10.004390, 49.973931, 5)

    pressure_values = np.linspace(25.027517, 49.956616, 5)

    time_values = np.linspace(2.367172, 33.293734, 5)

    # Optimization
    for ratio in ratio_values:

        # Calculate CO2 from H2 and Ratio
        co2 = h2 / ratio

        # Ignore values outside training range
        if co2 < 0.303735 or co2 > 1.795970:
            continue

        for temp in temp_values:

            for pressure in pressure_values:

                for time in time_values:

                    prediction = model.predict([[
                        co2,
                        h2,
                        temp,
                        pressure,
                        time,
                        ratio
                    ]])

                    if prediction[0] > best_methanol:

                        best_methanol = prediction[0]

                        best_conditions = {
                            "H2": h2,
                            "CO2": co2,
                            "Ratio": ratio,
                            "Temperature": temp,
                            "Pressure": pressure,
                            "TimeCost": time,
                            "PredictedMethanol": prediction[0]
                        }

    return best_conditions