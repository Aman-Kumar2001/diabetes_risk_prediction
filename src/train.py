import pandas as pd
import joblib


from src.preprocessing import preprocess_data
from src.model import build_model


def main():
    # Load training data
    
    data = pd.read_csv("data/raw/train.csv", index_col="id")

    y = data["diagnosed_diabetes"]
    X = data.drop(columns="diagnosed_diabetes")

    
    num_cols = [
        "age", "alcohol_consumption_per_week",
        "physical_activity_minutes_per_week", "diet_score",
        "sleep_hours_per_day", "screen_time_hours_per_day",
        "bmi", "waist_to_hip_ratio",
        "systolic_bp", "diastolic_bp", "heart_rate",
        "cholesterol_total", "hdl_cholesterol",
        "ldl_cholesterol", "triglycerides"
    ]

    ordinal_cat_cols = ["education_level", "income_level"]

    nominal_cat_cols = [
        "gender", "ethnicity",
        "smoking_status", "employment_status"
    ]

    # Build pipeline
    preprocessor = preprocess_data(
        num_cols=num_cols,
        ordinal_cat_cols=ordinal_cat_cols,
        nominal_cat_cols=nominal_cat_cols
    )

    model_pipeline = build_model(preprocessor)

    # Train on FULL data
    model_pipeline.fit(X, y)

    joblib.dump(model_pipeline, "artifacts/diabetes_model.pkl")

    print("Model training complete. Artifact saved.")


if __name__ == "__main__":
    main()
