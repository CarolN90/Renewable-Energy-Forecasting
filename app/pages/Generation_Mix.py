import streamlit as st
from utils.data_loader import load_energy_data
from utils.plots import plot_energy_mix_area, plot_energy_mix_percent

df = load_energy_data()

st.title("⚡ Energy Generation Mix")

st.plotly_chart(plot_energy_mix_area(df), use_container_width=True)
st.markdown("### % Share of Total Generation")
st.plotly_chart(plot_energy_mix_percent(df), use_container_width=True)
