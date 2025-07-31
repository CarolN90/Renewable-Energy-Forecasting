import pandas as pd
import os
import joblib

DATA_PATH = os.path.join("app", "data", "merged1_energy_data.csv")
MODEL_PATH = os.path.join("app", "models", "sarimax_results.pkl")

def load_energy_data():
    df = pd.read_csv(DATA_PATH, parse_dates=["Month"])
    df = df.set_index("Month").sort_index()
    return df

def load_model():
    return joblib.load(MODEL_PATH)
