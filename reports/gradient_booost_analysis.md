<h1> How correct Model is Selected</h1>

Performance Comparision of Logistic Regression, RandomForestClassifier and HistGradientBoostingClassifier

<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th>Model</th>
      <th>ROC-AUC</th>
      <th>Log Loss</th>
      <th>Remarks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Logistic Regression</td>
      <td>0.69</td>
      <td>0.63</td>
      <td>Baseline linear model</td>
    </tr>
    <tr>
      <td>Random Forest</td>
      <td>0.70</td>
      <td>0.60</td>
      <td>Better calibration, limited ranking gain</td>
    </tr>
    <tr>
      <td>Gradient Boosting</td>
      <td><strong>0.719</strong></td>
      <td><strong>0.588</strong></td>
      <td><strong>Best overall performance (selected)</strong></td>
    </tr>
  </tbody>
</table>


Based on above table, Gradient Boosting is a correct fit for the model.

The Precision–Recall curve for the Gradient Boosting model shows a consistent improvement over baseline models, maintaining precision levels of ~0.75–0.8.

After tuning the Gradient Boost model, we have our best parameters as follows :-

learning_rate = 0.1
max_iter = 300–500
max_depth = 5–6
min_samples_leaf = 20

Best ROC_AUC score obtained = 0.723
Best Log_loss score = 0.586