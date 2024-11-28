# utils/evaluation.py

import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import accuracy_score

def evaluate_models(models, X, y, n_splits=100, test_size=50):
    results = []
    sss = StratifiedShuffleSplit(n_splits=n_splits, test_size=test_size, random_state=42)
    
    for model_name, model_func in models.items():
        accuracies = []
        for train_index, test_index in sss.split(X, y):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]
            
            if 'NN_' in model_name:
                # Neural Network
                model = model_func()
                model.fit(X_train, y_train, epochs=50, batch_size=8, verbose=0)
                y_pred = (model.predict(X_test) > 0.5).astype("int32")
                y_pred = y_pred.flatten()
            else:
                # Classical Methods
                model = model_func
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)
            
            acc = accuracy_score(y_test, y_pred)
            accuracies.append(acc)
        
        avg_accuracy = np.mean(accuracies)
        results.append({'Model': model_name, 'Average Accuracy': avg_accuracy})
    
    results_df = pd.DataFrame(results)
    return results_df
