import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sys

# Add parent directory to system path for module access
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# --- Load data ---
@st.cache_data
def load_data():
    path = os.path.join("..", "data", "merged1_energy_data.csv")
    df = pd.read_csv(path)
    df["Month"] = pd.to_datetime(df["Month"])
    return df

df = load_data()

# Use most recent row as baseline
latest = df.iloc[-1]

# ✅ Correctly match actual column names (case-sensitive)
baseline = {
    "HYDRO": latest["HYDRO"],
    "WIND": latest["WIND"],
    "GEOTHERMAL": latest["GEOTHERMAL"],
    "SOLAR": latest["SOLAR"],
    "THERMAL": latest["Thermal"]  # Corrected column name
}

# --- Layout ---
st.title("🧪 Scenario Explorer: Renewable Energy Mix Simulator")
st.markdown("""
Adjust the sliders below to simulate a custom energy generation mix.
We'll compare your scenario to the current baseline and show the impact on total supply.
""")

# --- User sliders in sidebar ---
st.sidebar.header("🔧 Customize Energy Mix (GWh)")
user_inputs = {
    source: st.sidebar.slider(source, 0, int(baseline[source] * 2), int(baseline[source]))
    for source in baseline
}

# --- Comparison DataFrames ---
scenario_df = pd.DataFrame.from_dict(user_inputs, orient="index", columns=["User Scenario (GWh)"])
baseline_df = pd.DataFrame.from_dict(baseline, orient="index", columns=["Baseline (GWh)"])

comparison_df = pd.concat([baseline_df, scenario_df], axis=1)
comparison_df["Change (%)"] = 100 * (comparison_df["User Scenario (GWh)"] - comparison_df["Baseline (GWh)"]) / comparison_df["Baseline (GWh)"]

# --- Plot ---
st.subheader("🔍 Scenario vs Baseline Energy Mix")
fig = px.bar(
    comparison_df.reset_index(),
    x="index",
    y=["Baseline (GWh)", "User Scenario (GWh)"],
    barmode="group",
    labels={"index": "Energy Source"},
    title="Your Scenario Compared to Current Mix"
)
st.plotly_chart(fig, use_container_width=True)

# --- Interpretation block ---
st.markdown("### 📘 Interpretation")

total_baseline = baseline_df["Baseline (GWh)"].sum()
total_user = scenario_df["User Scenario (GWh)"].sum()
delta = total_user - total_baseline
percent_change = (delta / total_baseline) * 100

if percent_change > 0:
    st.success(f"🔼 Your scenario **increases** total generation by {percent_change:.1f}% (+{delta:.1f} GWh).")
elif percent_change < 0:
    st.warning(f"🔽 Your scenario **reduces** total generation by {abs(percent_change):.1f}% ({delta:.1f} GWh less).")
else:
    st.info("➖ Your scenario results in **no net change** in total energy generation.")

st.markdown("""
- ✅ Increasing renewables reduces reliance on thermal generation.
- ⚠️ Thermal sources (oil/diesel) are carbon-intensive and costly — reducing them supports climate goals.
- 🧪 Use this tool to model grid policy, investment targets, or Net-Zero pathways.
""")
