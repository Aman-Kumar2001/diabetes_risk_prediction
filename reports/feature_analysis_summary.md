<h1> Feature Analysis Summary </h1>

Following are the observations of the feature analysis :-

1. The features having low cardinality ( less than 4) have quite imbalanced variance or distribution, but all features are important and a case of rare categories.

2. Checking Correlation of the numerical columns, it is found mostly two features are having very high collinearity, they are cholesterol_total and ldl_cholesterol , and the other one is bmi and  waist_to_hip_ratio.

3. Also on checkong the redundant or data leakage, it is found no such features are available there.

4. We have also ckecked for near constant data, but no such feature is there, cardiovascular_history may be seen like that but it is an important feature and also can be seen as rare category data.

5. Test data also not having any missing values or extra columns, which needs to be handled.

6. Cardinality of categorical data checked, having some rare and quite imbalance data, which will be featured and handled in later processing.