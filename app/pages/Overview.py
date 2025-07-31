import streamlit as st
import pandas as pd
from utils.data_loader import load_energy_data
from utils.plots import plot_consumption_trend, show_summary_kpis

df = load_energy_data()

st.title("📊 Electricity Overview: Consumption & Trends")
show_summary_kpis(df)
st.plotly_chart(plot_consumption_trend(df), use_container_width=True)
