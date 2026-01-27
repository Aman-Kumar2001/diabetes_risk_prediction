from fastapi import FastAPI
from src.predict import predict_diabetes

app = FastAPI()

@app.post("/predict")
def predict(data : dict):
    prob = predict_diabetes(data)
    return {"diabetes_probability": prob}
