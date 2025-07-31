import streamlit as st

st.set_page_config(page_title="Kenya Energy Insights", layout="wide", page_icon="🔌")

st.title("🔌 Kenya Energy Intelligence Dashboard")
st.markdown("""
Welcome to a multi-layered analytical view of Kenya's electricity landscape.

Navigate through the tabs on the left:
- 📊 Overview: Key metrics and trends
- ⚡ Generation Mix: Renewable vs non-renewable evolution
- 🔮 Forecasting Tool: SARIMA-based monthly projections
- 🧪 Scenario Explorer: Test different renewable supply inputs
- 🌐 Grid Connectivity: Electrification and access insights
""")
