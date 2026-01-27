import joblib
import pandas as pd

model = joblib.load("artifacts/diabetes_model.pkl")

def predict_diabetes(input_dict):
    df = pd.DataFrame([input_dict])
    prob = model.predict_proba(df)[0, 1]
    return float(prob)
