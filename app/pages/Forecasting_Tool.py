
import sys
import os

# Add parent directory (where utils/ is) to the import path
PARENT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PARENT not in sys.path:
    sys.path.append(PARENT)

from utils.plots import forecast_chart  # ✅ should now work

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from utils.data_loader import load_energy_data
from utils.plots import forecast_chart

st.title("🔮 Electricity Demand Forecast")

df = load_energy_data()
model = joblib.load("app/models/sarimax_results.pkl")

selected_date = st.date_input(
    "Select forecast date", 
    min_value=df.index.max() + pd.DateOffset(months=1)
)

if st.button("Run Forecast"):
    horizon = (selected_date.year - df.index.max().year) * 12 + (selected_date.month - df.index.max().month)
    exog_vars = df[["HYDRO", "WIND", "SOLAR"]].iloc[-1:].values
    exog_future = np.tile(exog_vars, (horizon, 1))

    forecast = model.get_forecast(steps=horizon, exog=exog_future)
    pred = forecast.predicted_mean.iloc[-1]
    st.metric("Forecasted Consumption (GWh)", f"{pred:.1f}")
    st.plotly_chart(forecast_chart(df, selected_date, pred), use_container_width=True)
