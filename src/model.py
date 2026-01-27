import lightgbm as lgb
from sklearn.pipeline import Pipeline

def build_model(preprocessor):
    model = lgb.LGBMClassifier(
        objective="binary",
        n_estimators=800,
        learning_rate=0.05,
        num_leaves=31,
        min_child_samples=80,
        feature_fraction=0.7,
        bagging_fraction=0.9,
        random_state=1,
        n_jobs=-1
    )

    lgb_pipeline = Pipeline([
        ("preprocess", preprocessor),
        ("model", model)
    ])

    return lgb_pipeline
