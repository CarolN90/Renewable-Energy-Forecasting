import pandas as pd
import joblib

def load_energy_data():
    df = pd.read_csv("data/merged1_energy_data.csv", parse_dates=["Month"])
    df = df.set_index("Month").sort_index()
    return df

def load_model():
    return joblib.load("models/sarimax_results.pkl")
