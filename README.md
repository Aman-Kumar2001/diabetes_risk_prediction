<h1> Diabetes Risk Prediction – End-to-End ML Project </h1>

This project builds and deploys a machine learning system to predict the probability of diabetes using demographic, lifestyle, and clinical features. It covers the complete data science lifecycle — from data exploration and modeling to production-ready API deployment.

<h3>Problem Statement</h3>

Given patient health and lifestyle data, predict the probability of being diagnosed with diabetes.
The task is treated as a probabilistic binary classification problem and evaluated using ROC-AUC and Log Loss.

<h3> Modeling Approach</h3>

Performed EDA to understand feature distributions, imbalance, and correlations

Built robust preprocessing using scikit-learn Pipelines

Numerical scaling and imputation

Ordinal and nominal categorical encoding

Trained and compared multiple models:

Logistic Regression

Random Forest

Gradient Boosting

LightGBM (final model)

Used K-Fold cross-validation and prediction averaging to reduce variance

Carefully avoided data leakage throughout experimentation

Final offline ROC-AUC ≈ 0.72, with consistent leaderboard performance.

<h3> Deployment </h3>

The final LightGBM pipeline (preprocessing + model) is deployed as a FastAPI REST service using Render.

API Features

/predict endpoint (POST)

Accepts patient data as JSON

Returns diabetes risk probability

Input validation using Pydantic

Interactive API testing via Swagger UI (/docs)