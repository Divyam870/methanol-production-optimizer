"""Grid-search optimiser built on the trained methanol production model."""

from functools import lru_cache
from itertools import product
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

MODEL_PATH = Path(__file__).parent / "methanol_gbr_model.pkl"

# Order is exactly the order used when the model was fitted in GD_regressor.ipynb.
FEATURE_NAMES = [
    "FeedflowCO2in",
    "FeedflowH2in",
    "TEMPin",
    "PRESout",
    "TimeCost",
    "H2_CO2_Ratio",
]

# Search ranges based on the training data (320 rows, see GD_regressor.ipynb).
RATIO_VALUES = np.linspace(1.0, 10.3, 20)          # ~5th to 95th percentile
TEMP_VALUES = np.linspace(10.004390, 49.973931, 9)
PRESSURE_VALUES = np.linspace(25.027517, 49.956616, 9)
# The training maximum (~33.3 h) is an outlier, so search a practical range.
TIME_VALUES = np.linspace(2.367172, 10.0, 10)

CO2_MIN = 0.303735
CO2_MAX = 1.795970


@lru_cache(maxsize=1)
def _load_model():
    """Load the trained model once per process instead of on every request."""
    return joblib.load(MODEL_PATH)


def optimize(h2):
    """Return the feasible operating conditions with the highest predicted yield."""
    candidates = []
    for ratio, temp, pressure, time in product(
        RATIO_VALUES, TEMP_VALUES, PRESSURE_VALUES, TIME_VALUES
    ):
        co2 = h2 / ratio
        if CO2_MIN <= co2 <= CO2_MAX:
            candidates.append((co2, h2, temp, pressure, time, ratio))

    if not candidates:
        raise ValueError(
            f"No feasible CO₂ flow for H₂={h2:.2f}: "
            f"CO₂ must stay within [{CO2_MIN}, {CO2_MAX}]."
        )

    # One batched prediction is far faster than predicting row by row.
    X = pd.DataFrame(candidates, columns=FEATURE_NAMES)
    predictions = _load_model().predict(X)
    best_index = int(np.argmax(predictions))
    co2, _, temp, pressure, time, ratio = candidates[best_index]

    return {
        "H2": float(h2),
        "CO2": float(co2),
        "Ratio": float(ratio),
        "Temperature": float(temp),
        "Pressure": float(pressure),
        "TimeCost": float(time),
        "PredictedMethanol": float(predictions[best_index]),
    }
