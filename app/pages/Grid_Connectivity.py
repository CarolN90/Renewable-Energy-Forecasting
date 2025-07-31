import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sys

# Ensure access to parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Load data
@st.cache_data
def load_data():
    path = os.path.join("app", "data", "merged1_energy_data.csv")
    df = pd.read_csv(path)
    df["Month"] = pd.to_datetime(df["Month"])
    return df

df = load_data()

# ---- Layout ----
st.title("🌐 Grid Connectivity Insights")
st.markdown("Explore Kenya’s national electrification and transmission grid build-out over time.")

# ---- Metric Cards ----
latest = df.iloc[-1]
col1, col2, col3 = st.columns(3)
col1.metric("📈 New Customers (Latest)", f"{latest['Number_of_new_customers']:,.0f}")
col2.metric("🔌 Total Connections", f"{latest['Cummulative_Connections']:,.0f}")
col3.metric("🏠 Low Voltage Access", f"{latest['415/240V or 433/250V']:,.0f} MW")

st.markdown("---")

# ---- Trend: New Customer Connections Over Time ----
st.subheader("📅 Monthly New Customer Connections")
fig1 = px.line(df, x="Month", y="Number_of_new_customers", markers=True,
               title="Monthly New Electricity Customers", labels={"Number_of_new_customers": "New Customers"})
st.plotly_chart(fig1, use_container_width=True)

# ---- Trend: Cumulative Connections Over Time ----
st.subheader("📈 Cumulative Electricity Connections")
fig2 = px.line(df, x="Month", y="Cummulative_Connections", title="Growth in Electricity Access",
               labels={"Cummulative_Connections": "Cumulative Connections"})
st.plotly_chart(fig2, use_container_width=True)

# ---- Grid Infrastructure Overview ----
st.subheader("🛰️ Transmission Infrastructure Overview")

infra_cols = [
    "400 kV Ketraco",
    "220kv Ketraco & KenGen links",
    "132kv Ketraco",
    "Kplc",
    "220 kV",
    "132 kV",
    "66 kV",
    "33 kV",
    "11 kV",
    "Total HV and MV",
    "415/240V or 433/250V"
]

# Melt for multiseries line plot
df_melt = df[["Month"] + infra_cols].melt(id_vars="Month", var_name="Voltage Level", value_name="Capacity (MW)")
fig3 = px.line(df_melt, x="Month", y="Capacity (MW)", color="Voltage Level",
               title="Installed Capacity by Voltage Level")
st.plotly_chart(fig3, use_container_width=True)

st.caption("⚡ Data reflects both transmission (KETRACO) and distribution (KPLC) infrastructure build-out over time.")
