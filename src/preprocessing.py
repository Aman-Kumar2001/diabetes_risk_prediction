from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.pipeline import Pipeline


def preprocess_data(num_cols, ordinal_cat_cols, nominal_cat_cols):
    # handling numerical data
    num_pipeline = Pipeline(steps=[("imputing",SimpleImputer(strategy='median')),
                                ("scaling", StandardScaler())])

    #handling ordinhal Categories
    ordinal_pipeline = Pipeline(steps=[("imputing",SimpleImputer(strategy='most_frequent')),
                                    ("encoding",OrdinalEncoder(categories= [['No formal', 'Highschool','Graduate','Postgraduate'],['Low','Lower-Middle','Middle','Upper-Middle','High']]))])

    #handling nominal Categories
    nominal_pipeline = Pipeline(steps=[("imputing",SimpleImputer(strategy='most_frequent')),
                                    ("encoding",OneHotEncoder(handle_unknown='ignore', drop='first'))])

    #Creating a combined Column Transformer

    preprocessing = ColumnTransformer(transformers=[("num_processing",num_pipeline,num_cols),
                                                    ("ordinal_processing",ordinal_pipeline,ordinal_cat_cols),
                                                    ("nominal_processing",nominal_pipeline,nominal_cat_cols)])
    
    return preprocessing

