<h1> LightGBM Model Fitting and Analysis </h1>

Baseline LightGBM Performance

A baseline LightGBM model was trained using the existing preprocessing pipeline without additional feature engineering.

Validation ROC-AUC: ~0.724

Validation Log Loss: ~0.584


This represented a clear improvement over all previous models, including tuned sklearn Gradient Boosting, confirming LightGBM as the strongest model family for this dataset.


Hyperparameter Tuning - A controlled RandomizedSearchCV was performed, focusing on high-impact parameters:

num_leaves
min_child_samples
feature_fraction
bagging_fraction
learning_rate

Best CV ROC-AUC: ~0.726
Validation ROC-AUC: ~0.7245

