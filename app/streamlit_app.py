import streamlit as st

st.set_page_config(page_title="Kenya Energy Insights", layout="wide", page_icon="🔌")

st.title("🔌 Kenya Energy Intelligence Dashboard")
st.markdown("""
Welcome to a multi-layered analytical view of Kenya's electricity landscape.

<<<<<<< HEAD
Navigate through the tabs on the left:
- 📊 Overview: Key metrics and trends
- ⚡ Generation Mix: Renewable vs non-renewable evolution
- 🔮 Forecasting Tool: SARIMA-based monthly projections
- 🧪 Scenario Explorer: Test different renewable supply inputs
- 🌐 Grid Connectivity: Electrification and access insights
""")
=======
    late_tariff_cols = [
        "Small_Commercial_3_100per_kWh_1500per_kWh",
        "SC3_Bulk_Supply_1000per_kWh_1500per_kWh",
        "Commercial_Industrial_6___220_000_V",
        "Commercial_Industrial_7_SEZs",
        "E_Mobility",
    ]
    for col in late_tariff_cols:
        if col in df.columns:
            df[col] = df[col].fillna(0)

    df = df.fillna(method="ffill").fillna(method="bfill")

    # engineered
    df["Month_Num"] = df.index.month
    df["Is_Rainy_Season"] = df["Month_Num"].isin([4, 5, 10, 11]).astype(int)
    df["quarter"] = df.index.quarter
    df["Month_sin"] = np.sin(2 * np.pi * df["Month_Num"] / 12)
    df["Month_cos"] = np.cos(2 * np.pi * df["Month_Num"] / 12)

    df["lag_1"] = df["electricity_consumption_GWh"].shift(1)
    df["lag_2"] = df["electricity_consumption_GWh"].shift(2)
    df["lag_3"] = df["electricity_consumption_GWh"].shift(3)
    df["rolling_mean_3"] = df["electricity_consumption_GWh"].rolling(3).mean()
    df["rolling_mean_6"] = df["electricity_consumption_GWh"].rolling(6).mean()

    return df.fillna(method="bfill")

# ----------------------------------------------------------
# 1. Load data & SARIMA model
# ----------------------------------------------------------
@st.cache_resource(show_spinner="Loading SARIMA model…")
def load_sarima():
    return joblib.load("app/sarimax_results.pkl")

df_fe = safe_clean_and_engineer("app/merged1_energy_data.csv")
sarima_res = load_sarima()

# ----------------------------------------------------------
# 2. Specify energy features to use
# ----------------------------------------------------------
energy_exog_cols = ["HYDRO", "WIND", "SOLAR"]

# Ensure all selected columns exist
missing_cols = [col for col in energy_exog_cols if col not in df_fe.columns]
if missing_cols:
    st.error(f"❌ Missing required energy columns: {missing_cols}")
    st.stop()

k_exog = len(energy_exog_cols)

# ----------------------------------------------------------
# 3. Streamlit UI
# ----------------------------------------------------------
st.set_page_config(page_title="Kenya SARIMA Forecast", page_icon="⚡")
st.title("⚡ Kenya Electricity-Consumption Forecast")
st.markdown("Enter a future date to predict electricity consumption (GWh).")

selected_date = st.date_input(
    "📅 Select forecast date (must be after the latest data)",
    min_value=df_fe.index.max() + pd.DateOffset(months=1),
    value=df_fe.index.max() + pd.DateOffset(months=1)
)

if st.button("🔮 Forecast for selected date"):
    last_known_date = df_fe.index.max()
    selected_date = pd.to_datetime(selected_date).replace(day=1)
    horizon_months = (selected_date.year - last_known_date.year) * 12 + (selected_date.month - last_known_date.month)

    if horizon_months <= 0:
        st.error("Please choose a future date beyond the latest data.")
    else:
        forecast_dates = pd.date_range(last_known_date + pd.DateOffset(months=1), periods=horizon_months, freq="MS")

        if k_exog == 0:
            exog_future = None
        else:
            last_row = df_fe[energy_exog_cols].iloc[-1:].values
            exog_future = np.repeat(last_row, horizon_months, axis=0)

        # Forecast
        forecast_res = sarima_res.get_forecast(steps=horizon_months, exog=exog_future)
        preds = forecast_res.predicted_mean
        forecast_value = preds.iloc[-1]

        # Output
        st.subheader(f"Forecast for {selected_date.strftime('%B %Y')}")
        st.metric(label="Predicted Electricity Consumption (GWh)", value=f"{forecast_value:.1f}")

        # Plot
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df_fe.index,
            y=df_fe["electricity_consumption_GWh"],
            mode="lines",
            name="Historical",
            line=dict(color="royalblue")
        ))
        fig.add_trace(go.Scatter(
            x=[selected_date],
            y=[forecast_value],
            mode="markers+text",
            name="Forecast",
            marker=dict(color="firebrick", size=10),
            text=[f"{forecast_value:.1f} GWh"],
            textposition="top center"
        ))
        fig.update_layout(
            title="SARIMA Forecast vs Historical",
            xaxis_title="Date",
            yaxis_title="Electricity Consumption (GWh)",
            hovermode="x unified"
        )
        st.plotly_chart(fig, use_container_width=True)
>>>>>>> 4b79e871dbc2797401a6bf4cb55a6e15d044c68e
