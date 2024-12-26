import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

def handle_missing(data):
    # Impute missing values for numerical columns with the mean
    numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
    imputer = SimpleImputer(strategy='mean')

    imputed_numerical = imputer.fit_transform(data[numerical_columns])
    imputed_numerical_df = pd.DataFrame(
        imputed_numerical,
        columns=numerical_columns,
        index=data.index
    )

    # Impute missing values for categorical columns with the most frequent value
    categorical_columns = data.select_dtypes(include=['object']).columns
    imputer = SimpleImputer(strategy='most_frequent')
    imputed_categorical = imputer.fit_transform(data[categorical_columns])
    imputed_categorical_df = pd.DataFrame(
        imputed_categorical,
        columns=categorical_columns,
        index=data.index
    )

    # Combine numerical and categorical columns
    df_cleaned = pd.concat([imputed_numerical_df, imputed_categorical_df], axis=1)

    # Reinsert all-NaN columns with default value
    for col in data.columns:
        if col not in df_cleaned.columns:
            df_cleaned[col] = np.nan

    return df_cleaned