# models/classification_methods.py

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.base import BaseEstimator, ClassifierMixin
import numpy as np

def get_classification_models():
    models = {
        'LDA': LinearDiscriminantAnalysis(),
        'QDA': QuadraticDiscriminantAnalysis(),
        'SVM': SVC(kernel='rbf', probability=True),
        'Naive_Bayes': GaussianNB(),
        # Add RDA if implemented
        # 'RDA': RegularizedDiscriminantAnalysis()
    }
    return models

# Optional: Implement RDA if needed
# class RegularizedDiscriminantAnalysis(BaseEstimator, ClassifierMixin):
#     def __init__(self, alpha=0.5):
#         self.alpha = alpha
#         # Add implementation details here
#     def fit(self, X, y):
#         pass
#     def predict(self, X):
#         pass
