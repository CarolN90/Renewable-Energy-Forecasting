import plotly.graph_objects as go
import plotly.express as px

def plot_consumption_trend(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df["electricity_consumption_GWh"], mode="lines", name="Consumption"))
    fig.update_layout(title="Electricity Consumption Over Time")
    return fig

def show_summary_kpis(df):
    st.metric("Latest Monthly Consumption (GWh)", f"{df['electricity_consumption_GWh'].iloc[-1]:.1f}")
    st.metric("Total Annual Consumption (GWh)", f"{df['electricity_consumption_GWh'].resample('Y').sum().iloc[-1]:,.0f}")

def plot_energy_mix_area(df):
    return px.area(df, x=df.index, y=["HYDRO", "SOLAR", "WIND"], title="Renewable Generation Over Time")

def plot_energy_mix_percent(df):
    df_pct = df[["HYDRO", "WIND", "SOLAR"]].div(df[["HYDRO", "WIND", "SOLAR"]].sum(axis=1), axis=0)
    return px.area(df_pct, x=df.index, y=df_pct.columns, title="Renewables % of Total Generation")

def forecast_chart(df, forecast_date, value):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df["electricity_consumption_GWh"], mode="lines", name="Historical"))
    fig.add_trace(go.Scatter(x=[forecast_date], y=[value], mode="markers+text", name="Forecast", text=[f"{value:.1f}"], textposition="top center"))
    return fig

def plot_grid_connectivity(df):
    if "grid_connections" in df.columns:
        return px.line(df, x=df.index, y="grid_connections", title="Grid Connections Over Time")
    else:
        return go.Figure().add_annotation(text="No connectivity data found")
