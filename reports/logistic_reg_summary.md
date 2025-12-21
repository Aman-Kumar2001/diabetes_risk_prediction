<h1> Base Model Analysis using Logistic Regression</h1>

A simple python file has been created, to create a pipeline for the preprocessing of the data.

Then a base model is trained for the data, using Logistic Regression.

ROC_AUC score comes out to be = 0.69, which is a good sign that the model is learning from the data.
Log_Loss comes out to be 0.63.

Confusion matrix using a thresholg of 0.5, is not givibg a good result, needs tuning. 
PR curve also shows the same that threshold needs to be tuned.

Coefficients of Logistic Regression model has been observed for the features.
- Some features are strongly related in increasing the diabetes risk - positive values, eg - family diabetes history, age and so.
- Some features acting as protective feature, high negative values - eg - physical activity, diet score and so.