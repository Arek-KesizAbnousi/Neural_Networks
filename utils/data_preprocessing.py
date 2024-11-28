# utils/data_preprocessing.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data(filepath):
    # Load data
    df = pd.read_csv(filepath, header=None)
    
    # Separate features and target
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values
    
    # Apply logarithmic transformation
    X = np.log1p(X)
    
    # Encode target variable
    le = LabelEncoder()
    y = le.fit_transform(y)
    
    return X, y
