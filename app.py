from fastapi import FastAPI
from src.predict import predict_diabetes
from pydantic import BaseModel

class Patient(BaseModel):
    age: int
    alcohol_consumption_per_week: float
    physical_activity_minutes_per_week: float
    diet_score: float
    sleep_hours_per_day: float
    screen_time_hours_per_day: float
    bmi: float
    waist_to_hip_ratio: float
    systolic_bp: int
    diastolic_bp: int
    heart_rate: int
    cholesterol_total: float
    hdl_cholesterol: float
    ldl_cholesterol: float
    triglycerides: float

    gender: str
    ethnicity: str
    education_level: str
    income_level: str
    smoking_status: str
    employment_status: str

    family_history_diabetes: int
    hypertension_history: int
    cardiovascular_history: int


app = FastAPI()

@app.post("/predict")
def predict(data: Patient):
    prob = predict_diabetes(data.model_dump())
    return {"diabetes_probability": prob}
